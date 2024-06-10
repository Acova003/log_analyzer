import click
import pandas as pd
import logging
import json
import numpy as np
import io

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class NpEncoder(json.JSONEncoder):
    """
    Custom JSON encoder for NumPy data types.

    This encoder extends the default JSONEncoder to handle NumPy data types, 
    which are not natively serializable by the standard json library. It converts 
    NumPy integers, floats, arrays, and datetime64 objects to their corresponding 
    Python native types, ensuring they can be serialized to JSON without errors.

    - np.datetime64 and np.complexfloating are converted to strings.
    - np.integer is converted to int.
    - np.floating is converted to float.
    - np.ndarray is converted to a list, with special handling for datetime64 and 
      complexfloating elements.
    """
    def default(self, obj):
        dtypes = (np.datetime64, np.complexfloating)
        if isinstance(obj, dtypes):
            return str(obj)
        elif isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            if any([np.issubdtype(obj.dtype, i) for i in dtypes]):
                return obj.astype(str).tolist()
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def preprocess_line(line):
    fields = line.split()
    # Check if the line has more fields than expected
    if len(fields) > 10:
        logging.error(f"Bad line with extra fields: {line.strip()}")
        click.echo(f"Skipping bad line: {line.strip()}")
        return None
    return line

def handle_bad_lines(bad_line):
    logging.error(f"Skipping bad line: {bad_line}")

@click.command()
@click.option('--input', 'inputs', type=click.Path(exists=True), multiple=True, required=True, help='Path to input file(s)')
@click.argument('output', type=click.Path())  # Positional argument for output file
@click.option('--mfip', is_flag=True, help='Most frequent IP')
@click.option('--lfip', is_flag=True, help='Least frequent IP')
@click.option('--eps', is_flag=True, help='Events per second')
@click.option('--bytes', is_flag=True, help='Total amount of bytes exchanged')
def analyze(inputs, output, mfip, lfip, eps, bytes):
    """
    Analyze log files and perform the following operations in options

    Arguments:
        input: Path to one or more input files.
        output: Path to a file to save output in plain text JSON format.
    Options:
        --mfip: most frequent IP
        --lfip: least frequent IP
        --eps: events per second
        --bytes: total amount of bytes exchanged
    """
    try:
        df_list = []
        for file in inputs:
            logging.debug(f"Reading file: {file}")
            try:
                with open(file, 'r') as f:
                    lines = f.readlines()
                
                valid_lines = []
                for line in lines:
                    processed_line = preprocess_line(line)
                    if processed_line:
                        valid_lines.append(processed_line)
                
                if not valid_lines:
                    logging.error(f"No valid lines in file: {file}")
                    continue
                
                df = pd.read_csv(io.StringIO('\n'.join(valid_lines)), sep=r'\s+', header=None, names=[
                    'timestamp', 'response_header_size', 'client_ip', 'http_response_code',
                    'response_size', 'http_request_method', 'url', 'username',
                    'type_of_access', 'response_type'
                ], on_bad_lines=handle_bad_lines, engine='python')
                df_list.append(df)
            except pd.errors.ParserError as e:
                logging.error(f"Error parsing file {file}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error reading file {file}: {e}")
        
        if not df_list:
            click.echo("No valid data to process.")
            return
        
        df = pd.concat(df_list)
        logging.debug("Data concatenation complete.")

        # Log to see if the data is correct
        logging.debug("\n" + df.head().to_string(index=False))  # Log only the first few rows to avoid clutter

        results = {}

        if mfip or lfip:
            ip_counts = df['client_ip'].value_counts()
            if mfip:
                most_freq_ip = ip_counts.idxmax()
                results['most_frequent_ip'] = most_freq_ip
                logging.debug(f"Most frequent IP: {most_freq_ip}")
            
            if lfip:
                least_freq_ip = ip_counts.idxmin()
                results['least_frequent_ip'] = least_freq_ip
                logging.debug(f"Least frequent IP: {least_freq_ip}")

        # Average of events per second
        if eps:
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
            df['timestamp'] = df['timestamp'].dt.floor('s')
            eps = df.groupby('timestamp').size().mean()
            results['events_per_second'] = float(eps)  
            logging.debug(f"Events per second: {eps}")

        if bytes:
            total_bytes = df['response_size'].sum()
            results['total_bytes'] = int(total_bytes)  
            logging.debug(f"Total bytes exchanged: {total_bytes}")

        # Write the results to the output file
        with open(output, 'w') as f:
            json.dump(results, f, indent=4, cls=NpEncoder)

        click.echo(f"Output written to {output}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        click.echo(f"An error occurred: {e}")

if __name__ == '__main__':
    analyze()

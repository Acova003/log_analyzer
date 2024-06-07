import click
import pandas as pd
import logging
import json

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


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
            df = pd.read_csv(file, sep=r'\s+', header=None, names=[
                'timestamp', 'response_header_size', 'client_ip', 'http_response_code',
                'response_size', 'http_request_method', 'url', 'username',
                'type_of_access', 'response_type'
            ])
            df_list.append(df)
        df = pd.concat(df_list)

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
            results['events_per_second'] = eps
            logging.debug(f"Events per second: {eps}")
                    
        # Write the results to the output file
        with open(output, 'w') as f:
            json.dump(results, f, indent=4)

        click.echo(f"Output written to {output}")


    except Exception as e:
        click.echo(f"An error occurred: {e}")

if __name__ == '__main__':
    analyze()

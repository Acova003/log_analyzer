import click

click.command()
@click.option('--input', 'inputs', type=click.Path(exists=True), multiple=True, required=True, help='Path to input file(s)')
@click.argument('output', type=click.Path()) # Positional argument for output file
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
        pass
        # Read the data into a dataframe with pandas?
    
    #Exceptions that we should catch
    except:
        pass

if __name__ == '__main__':
    analyze()
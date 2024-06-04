import click

click.command()
@click.option('--input', 'inputs', type=click.Path(exists=True), multiple=True, required=True, help='Path to input file(s)')
@click.argument('output', type=click.Path()) # Positional argument for output file
@click.option('--mfip', is_flag=True, help='Most frequent IP')
@click.option('--lfip', is_flag=True, help='Least frequent IP')
@click.option('--eps', is_flag=True, help='Events per second')
@click.option('--bytes', is_flag=True, help='Total amount of bytes exchanged')
def analyze(inputs, output, mfip, lfip, eps, bytes):
    pass

if __name__ == '__main__':
    analyze()
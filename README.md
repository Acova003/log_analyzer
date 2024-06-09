# Log Analyzer CLI Tool

This is a command-line tool to analyze the content of log files. The tool accepts the log file location and operation(s) as input arguments and returns the results of the operations as output. 

## Features

- Most frequent IP address (`--mfip`)
- Least frequent IP address (`--lfip`)
- Events per second (`--eps`)
- Total amount of bytes exchanged (`--bytes`)

## Requirements

- Python >= 3.11
- Docker (optional, for running the tool in a container)

## Installation

### Running Locally

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/Acova003/log_analyzer.git
    cd log_analyzer
    ```

2. **Create and Activate Virtual Environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the CLI Tool**:

    ```sh
    python log_analyzer/cli.py --input path/to/access.log path/to/output.json <OPTIONS: --mfip --lfip --eps --bytes>
    ```

### Running with Docker

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/Acova003/log_analyzer.git
    cd log_analyzer
    ```

2. **Build the Docker Image**:

    ```sh
    docker build -t log_analyzer .
    ```

3. **Run the Docker Container**:

    ```sh
    docker run --rm -v path/to/local/directory:/data log_analyzer --input /data/access.log /data/output.json --mfip --lfip --eps --bytes
    ```

    The output file `output.json` will be created in the `path/to/local/directory` on your host machine.

## Usage

### Arguments:

- `--input`: Path to one or more input files. This argument is required.
- `output`: Path to a file to save output in plain text JSON format. This argument is required.

### Options:

- `--mfip`: Calculate the most frequent IP address.
- `--lfip`: Calculate the least frequent IP address.
- `--eps`: Calculate events per second.
- `--bytes`: Calculate the total amount of bytes exchanged.

### Examples:

**Running Locally**:

```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --mfip
```

**Running with Docker**:

```sh
docker run --rm -v path/to/local/directory:/data log_analyzer --input /data/access.log /data/output.json --eps
```


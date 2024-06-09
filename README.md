# Log Analyzer CLI Tool

This is a command-line tool to analyze the content of log files. The tool accepts the log file location(s) and operation(s) as input arguments and returns the results of the operations as output. 

## Features

- Calculate the most frequent IP address (`--mfip`)
- Calculate the least frequent IP address (`--lfip`)
- Calculate events per second (`--eps`)
- Calculate the total amount of bytes exchanged (`--bytes`)

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
    python log_analyzer/cli.py --input path/to/access.log path/to/output.json --mfip --lfip --eps --bytes
    ```

    - Replace `path/to/access.log` with the actual path to your log file.
    - Replace `path/to/output.json` with the desired path for the output JSON file.

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

    - Replace `path/to/local/directory` with the actual path to the local directory where your log file is located.
    - Ensure the log file (`access.log`) is in the directory specified.
    - The output file `output.json` will be created in the specified local directory.

## Usage

### Arguments:

- `--input`: Path to one or more input files. This argument is required.
- `output`: Path to a file to save output in plain text JSON format. This argument is required.

### Options:

- `--mfip`: Calculate the most frequent IP address.
- `--lfip`: Calculate the least frequent IP address.
- `--eps`: Calculate events per second.
- `--bytes`: Calculate the total amount of bytes exchanged.

### Using Option Flags

You can use the option flags to specify which operations to perform on the log files. Multiple option flags can be combined to perform multiple operations at once.

#### Example Commands:

- Replace `path/to/access.log` with the actual path to your log file.
- Replace `path/to/output.json` with the desired path for the output JSON file.

**Calculate the most frequent IP address**:
```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --mfip
```

**Calculate the least frequent IP address**:
```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --lfip
```

**Calculate events per second**:
```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --eps
```

**Calculate the total amount of bytes exchanged**:
```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --bytes
```

**Combined operations**:
```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --mfip --lfip --eps --bytes
```

### Examples:

**Running Locally**:
- Replace path/to/access.log with the actual path to your log file.
- Replace path/to/output.json with the desired path for the output JSON file.

```sh
python log_analyzer/cli.py --input path/to/access.log path/to/output.json --mfip
```

**Running with Docker**:
- Replace path/to/local/directory with the actual path to the local directory where your log file is located.
- Ensure the log file (access.log) is in the directory specified.
- The output file output.json will be created in the specified local directory.

```sh
docker run --rm -v path/to/local/directory:/data log_analyzer --input /data/access.log /data/output.json --eps
```






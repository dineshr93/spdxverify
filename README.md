# SPDX Verify

This repository contains standalone command for verifying SPDX (Software Package Data Exchange) documents.

## Note
[NOT-SUPPORTED SPDX 3.0 https://github.com/spdx/tools-python/issues/760]

## Features

- Validate SPDX documents for compliance with the specification.
- Check for completeness and correctness of SPDX metadata.
- Support for multiple SPDX formats (e.g., RDF, JSON, Tag/Value).

## Prerequisites

- Python 3.8 or higher
- Required dependencies (see `pyproject.toml`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dineshr93/spdxverify.git
    cd spdxverify
    ```

2. Install dependencies:
    ```bash
    pip install spdxverify
    ```

## Usage

Run the verification tool on an SPDX file:
```bash
> spdxverify -h
usage: spdxverify [-h] spdxFileorDir

Validate SPDX file

positional arguments:
  spdxFileorDir  SPDX File or SPDX Folder path[NOT-SUPPORTED SPDX 3.0 https://github.com/spdx/tools-python/issues/760]

options:
  -h, --help     show this help message and exit
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## References

- [SPDX Specification](https://spdx.dev/specifications/)
- [SPDX Tools](https://github.com/spdx/tools-python)

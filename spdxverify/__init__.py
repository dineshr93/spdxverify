import logging
import os
import sys
from spdx_tools.spdx.parser.parse_anything import parse_file
from typing import List
from spdx_tools.spdx.validation.document_validator import validate_full_spdx_document
from spdx_tools.spdx.validation.validation_message import ValidationMessage
import argparse
from spdx_tools.spdx.model import (Document)
from spdx_tools.spdx.formats import FileFormat, file_name_to_format


def validate_spdx_document(INPUT_FILE: str) -> None:
        
        spdx_doc:Document = parse_file(INPUT_FILE)

        spdx_doc = parse_file(INPUT_FILE)
        validation_messages: List[ValidationMessage] = validate_full_spdx_document(spdx_doc)
        is_valid = True

        # You can have a look at each entry's message and context (like spdx_id, parent_id, full_element)
        # which will help you pinpoint the location of the invalidity.
        for message in validation_messages:
            is_valid = False
            print(message.validation_message)

        if is_valid:
            print(f"The SPDX document {INPUT_FILE} is valid.")
        else:
            print(f"The SPDX document {INPUT_FILE} is NOT valid.")

def is_valid_file_format(INPUT_FILE: str) -> bool:
    input_format = file_name_to_format(INPUT_FILE)
    is_valid = input_format in [
                            FileFormat.RDF_XML,
                            FileFormat.TAG_VALUE,
                            FileFormat.JSON,
                            FileFormat.XML,
                            FileFormat.YAML,
                            ]   
    if not is_valid_file_format:
        logging.warning(f"Unsupported file format for file: {INPUT_FILE}")
        sys.exit(1)
    return is_valid

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Validate SPDX file")
    parser.add_argument("spdxFileorDir", help="SPDX File or SPDX Folder path[NOT-SUPPORTED SPDX 3.0 https://github.com/spdx/tools-python/issues/760]")
    args = parser.parse_args()

    INPUT_FILE = args.spdxFileorDir
    
    if os.path.isfile(INPUT_FILE):
        if is_valid_file_format(INPUT_FILE):
            validate_spdx_document(INPUT_FILE)

    elif os.path.isdir(INPUT_FILE):
        for root, dirs, files in os.walk(INPUT_FILE):
            for file in files:
                file_path = os.path.join(root, file)
                if is_valid_file_format(file_path):
                    validate_spdx_document(file_path)
    else:
        logging.error("Path does not exist or is neither file nor folder")

if __name__ == "__main__":
    main()


import re

from os import path


def copy_file(command: str) -> None:
    # string must be like "cp {input_file} {output_file}"
    command_pattern = re.compile(
        r"^cp\s+([A-Za-z0-9_.-]+)\s+(?!\1$)([A-Za-z0-9_.-]+)$"
    )

    if not command_pattern.match(command):
        return

    input_filename = command.split(" ")[1]
    output_filename = command.split(" ")[2]

    if input_filename == output_filename or not path.exists(input_filename):
        return

    with (
        open(input_filename, "r") as input_file,
        open(output_filename, "w") as output_file
    ):
        output_file.write(input_file.read())

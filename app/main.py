"""
I thought that such decisions might not be fair

import subprocess
def copy_file(command: str):
    subprocess.run(command, shell=True)

import os
def copy_file(command: str):
    os.system(command)
"""


def copy_file(command: str) -> None:
    if command[:3] == "cp":
        raise ValueError(
            "Expected 'cp' as the first argument"
        )
    command = command[3:]
    source_parts = command.split(".")

    source_file = source_parts[0] + "." + source_parts[1].split()[0]
    destination_file = command[len(source_file) + 1:]

    if not destination_file or len(destination_file.split(".")) > 2:
        raise ValueError(
            "Expected 3 arguements"
        )

    if source_file != destination_file:
        with (
            open(source_file, "r") as source,
            open(destination_file, "w") as destination
        ):
            destination.write(source.read())

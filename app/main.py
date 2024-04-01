"""
I thought that such decisions might not be fair

import subprocess
def copy_file(command: str):
    subprocess.run(command, shell=True)

import os
def copy_file(command: str):
    os.system(command)
"""

import shlex


def copy_file(command: str) -> None:
    if command[:3] == "cp":
        raise ValueError(
            "Expected 'cp' as the first argument"
        )

    source_parts = shlex.split(command[3:])

    if len(source_parts) != 2:
        raise ValueError(
            "Expected 2 arguements"
        )

    if source_parts[0] != source_parts[1]:
        with (
            open(source_parts[0], "r") as source,
            open(source_parts[1], "w") as destination
        ):
            destination.write(source.read())

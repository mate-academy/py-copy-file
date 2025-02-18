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

    source_path, destination_path, *extra_path = shlex.split(command[3:])

    if extra_path:
        raise ValueError(
            "Expected 2 arguements"
        )

    if source_path != destination_path:
        with (
            open(source_path, "r") as source,
            open(destination_path, "w") as destination
        ):
            destination.write(source.read())

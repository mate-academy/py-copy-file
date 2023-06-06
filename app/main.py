from shutil import copy


def copy_file(command: str) -> None:
    comm_data = command.split()
    if len(comm_data) == 3 and comm_data[-1] != comm_data[-2]:
        copy(comm_data[-2], comm_data[-1])

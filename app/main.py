from shutil import copy


def copy_file(command: str) -> None:
    comm_data = command.split()
    if comm_data[-1] == comm_data[-2]:
        return
    copy(comm_data[-2], comm_data[-1])

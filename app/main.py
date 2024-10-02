from contextlib import contextmanager


@contextmanager
def open_file(name: str, method: str) -> None:
    func = open(name, method)
    try:
        yield func
    finally:
        func.close()


def copy_file(command: str) -> None:
    command = command.split()
    if command[0] != "cp":
        return
    if command[1] == command[2]:
        return
    with (
        open_file(command[1], "r") as file_in,
        open_file(command[2], "x") as file_out,
    ):
        file_out.write(file_in.read())

command = "cp file.txt new_file.txt"


def copy_file(command: str) -> None:
    command = command.split(" ")
    if command[0] != "cp" or len(command) != 3 or command[1] == command[2]:
        return None

    try:
        with (
            open(command[1], "r") as file_in,
            open(command[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return None

class InvalidCommandFormat(Exception):
    pass


def copy_file(command: str) -> None:
    command = command.split()

    if command[0] != "cp":
        raise InvalidCommandFormat(
            "Please provide a command like 'cp file.txt file-copy.txt'"
        )

    if command[1] != command[2]:
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            content = file_in.read()
            file_out.write(content)
            print("OK")

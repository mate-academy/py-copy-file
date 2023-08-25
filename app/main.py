class InvalidCommandFormat(Exception):
    pass


def copy_file(command: str) -> None:
    command, old_file, copy_file = command.split()

    if command != "cp":
        raise InvalidCommandFormat(
            "Please provide a command like 'cp file.txt file-copy.txt'"
        )

    if old_file != copy_file:
        with (open(old_file, "r") as file_in,
              open(copy_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
            print("OK")

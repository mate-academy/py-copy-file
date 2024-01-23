class ErrorCopyFile(Exception):
    pass


def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ErrorCopyFile("Wrong command. Command must include 3 arguments.")

    file_from = command.split()[1]
    file_to = command.split()[2]

    with open(file_from, "r") as file_in, open(file_to, "w") as file_out:
        file_out.write(file_in.read())

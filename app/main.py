class SameNameError(NameError):
    pass


def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Error: Invalid command format. "
                         "Please use 'cp file copy_file'")

    with (open(parts[1], "r") as file_origin,
          open(parts[2], "w") as file_copy):

        text = file_origin.read()

        while True:

            if parts[1] == parts[2]:
                raise SameNameError("Copy cannot have the same name!")

            file_copy.write(text)


if __name__ == "__main__":
    copy_file()

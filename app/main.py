def copy_file(command: str) -> None:
    try:
        command, file_to_copy, new_file = command.split()

        if command == "cp" and file_to_copy != new_file:
            with (
                open(file_to_copy, "r") as file_to_copy,
                open(new_file, "w") as new_file

            ):
                new_file.write(file_to_copy.read())

    except FileNotFoundError:
        print("File to copy does not exist")
    except ValueError:
        print("Incorrect command input")

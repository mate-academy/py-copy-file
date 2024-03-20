def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        print("Command not found")
        return

    command, file_name, new_file_name = command.split()

    if not any(("copy" in command, "cp" in command)):
        print("Command not found")
        return

    if file_name != new_file_name:
        try:
            with (
                open(file_name, "r") as old_file,
                open(new_file_name, "w") as new_file
            ):

                new_file.write(old_file.read())

        except FileNotFoundError:
            print("File not found")

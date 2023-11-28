def copy_file(command: str) -> None:
    command, file_name, new_file_name = command.split(" ")

    if file_name != new_file_name:
        try:
            with open(file_name, "r") as old, open(new_file_name, "w") as new:
                new.write(old.read())

        except FileNotFoundError:
            print("File not found")

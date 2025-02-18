def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command format")
        return

    command, first_name, second_name = command.split()
    if first_name != second_name and command == "cp":
        try:
            with (open(first_name, "r") as file_in,
                    open(second_name, "w") as file_out):
                file_out.write(file_in.read())
        except OSError:
            print("File not found")

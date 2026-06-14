def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    try:
        if len(command_parts) != 3:
            raise ValueError("Invalid command: cp <original_file> <new_file>")
        cmd, source, copy = command_parts
        if cmd != "cp":
            raise ValueError("Invalid command: command must be 'cp'")
        if source != copy:
            with open(source, "r") as file_in, open(copy, "w") as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)

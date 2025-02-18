def copy_file(command: str) -> None:
    try:
        command_items = command.split()
        verify_command(command_items)

        if command_items[1] != command_items[-1]:
            with open(command_items[1], "r") as input_file, \
                    open(command_items[-1], "w") as output_file:
                output_file.write(input_file.read())

    except AttributeError:
        print("Command must be string in format 'cp {file_name} {copy_name}'.")
    except (ValueError, FileNotFoundError) as err:
        print(err)


def verify_command(command: list[str]) -> None:
    if not command:
        raise ValueError("No command has been given.")
    if command[0] != "cp":
        raise ValueError("Command must start with 'cp' keyword.")
    if len(command) <= 1:
        raise ValueError("No file arguments has been given.")
    if len(command) > 3:
        raise ValueError("Excessive file arguments has been given.")

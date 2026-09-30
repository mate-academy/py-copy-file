def copy_file(
    command: str
) -> None:
    file_content = ""
    command_array = command.split(" ")
    try:
        if len(command_array) != 3:
            raise ValueError("Not enough values in command.")
        if (
            command_array[0] == "cp"
            and command_array[1] != command_array[2]
        ):
            with (
                open(command_array[1], "r") as source_file,
                open(command_array[2], "w") as destination_file
            ):
                file_content = source_file.read()
                destination_file.write(file_content)
    except ValueError:
        print("Please, the command must have exactly 3 values.")
    except FileNotFoundError:
        print("File not found.")

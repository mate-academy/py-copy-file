def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError("Invalid command format. "
                         "Please provide the command in the format:"
                         " cp <source_file> <destination_file>")

    command_name, source_file, test_file = parts

    if source_file == test_file or command_name != "cp":
        raise ValueError("Source and destination files have the same name. "
                         "No action taken.")

    try:

        with (open(source_file, "r") as file_in,
              open(test_file, "w") as file_out):
            file_out.write(file_in.read())

        print(f"File '{source_file}' copied to '{test_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: One or both of the files "
              f"'{source_file}' and '{test_file}' not found.")

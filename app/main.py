def copy_file(command: str) -> None:
    try:
        input_command, input_file_name, output_file_name = command.split()
    except ValueError:
        raise ValueError(
            "Check if the command has the format: cp file.txt file_copy.txt"
        )
    if input_command != "cp":
        raise ValueError("The command must start with 'cp'")
    if input_file_name == output_file_name:
        raise ValueError("The file copy must have different name")
    with (
        open(input_file_name, "r") as file_in,
        open(output_file_name, "w") as file_out
    ):
        file_out.write(file_in.read())

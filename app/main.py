def copy_file(command: str) -> None:
    _, input_file_name, output_file_name = command.split()
    if input_file_name == output_file_name:
        return
    with open(input_file_name, "r") as file_in, \
            open(output_file_name, "w") as file_out:
        file_out.write(file_in.read())

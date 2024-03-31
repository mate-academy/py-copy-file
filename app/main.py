def copy_file(command: str) -> None:
    if len(command.split(" ")) < 3:
        raise TypeError("Incorrect command format")

    cp_command, input_file_name, output_file_name = command.split(" ")
    if input_file_name != output_file_name:
        with (open(input_file_name, "r") as file_in,
              open(output_file_name, "w") as file_out):
            file_out.write(file_in.read())


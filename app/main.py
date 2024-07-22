def copy_file(command: str) -> None:
    command_name, input_file, output_file, *_ = command.split()
    if command_name == "cp" and input_file != output_file:
        with (open(input_file, "r") as file_in,
              open(output_file, "w") as file_out):
            file_out.write(file_in.read())

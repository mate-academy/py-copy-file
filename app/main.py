def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3:
        command, input_file, output_file = parts
        if command != "cp" or input_file == output_file:
            return
        with (open(input_file, "r") as file_in,
              open(output_file, "w") as file_out):
            file_out.write(file_in.read())
    return

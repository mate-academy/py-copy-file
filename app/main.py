def copy_file(command: str) -> None | bool:
    input_file, output_file = command.split()[1:3]
    if input_file != output_file:
        with (open(input_file, "r") as file_in,
              open(output_file, "w") as file_out):
            file_out.write(file_in.read())
    return

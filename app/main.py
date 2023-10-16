def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3:
        function, input_file, output_file = command
        if function != "cp" or input_file == output_file:
            return
        with (open(input_file, "r") as file_in,
              open(output_file, "w") as file_out):
            file_out.write(file_in.read())
    return

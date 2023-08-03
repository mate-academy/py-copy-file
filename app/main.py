def copy_file(command: str) -> None:
    command_name, filename, copy_filename = command.split()

    if command_name == "cp" and filename != copy_filename:
        with (open(filename, "r") as file_in,
              open(copy_filename, "a") as file_out):
            for line in file_in:
                file_out.write(line)

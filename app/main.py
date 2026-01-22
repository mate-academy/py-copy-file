def copy_file(command: str) -> None:
    command, file_in_name, file_out_name = command.split()
    if command == "cp":
        if file_in_name == file_out_name:
            return
        with (open(file_in_name, "r")
              as file_in,
              open(file_out_name, "w")
              as file_out):
            for line in file_in:
                file_out.write(line)

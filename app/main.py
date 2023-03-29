def copy_file(command: str) -> None:
    command, current_file, new_file = command.split()
    if (current_file != new_file
            and command == "cp" and (current_file, new_file)):
        with (open(current_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())

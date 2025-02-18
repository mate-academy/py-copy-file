def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if old_file != new_file and command == "cp":
        with (open(old_file, "r") as file_out,
              open(new_file, "w") as file_in):
            file_in.write(file_out.read())

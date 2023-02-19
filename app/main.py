def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if old_file != new_file and command == "cp":
        with (open(f"../{old_file}", "r") as file_in,
              open(f"../{new_file}", "w") as file_out):
            file_out.write(file_in.read())

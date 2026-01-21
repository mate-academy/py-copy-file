def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        return "Command must be exactly 3 characters"
    command_name, initial_file, final_file = command_split
    if initial_file != final_file and command == "cp":
        with (open(initial_file, "r") as file_old,
              open(final_file, "w") as file_new):
            file_new.write(file_old.read())

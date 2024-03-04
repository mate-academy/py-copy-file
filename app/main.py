def copy_file(command: str) -> bool:
    commands = command.split()
    if len(commands) == 3 and commands[0] == "cp":
        _, cp_file, new_file = commands

        if cp_file != new_file:
            with (open(cp_file, "r") as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())

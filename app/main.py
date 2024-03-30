def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) == 3:
        cp, copied_file, new_file = commands
        if cp == "cp" and copied_file != new_file:
            with (open(copied_file, "r") as c_file,
                  open(new_file, "w") as n_file):
                n_file.write(c_file.read())

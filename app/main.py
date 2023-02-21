
def copy_file(command: str) -> None:
    command_name = command.split()[0]
    base_filename = command.split()[1]
    new_filename = command.split()[2]

    if command_name == "cp" and base_filename != new_filename:
        with (open(base_filename, "r") as base_file,
              open(new_filename, "w") as new_file):
            new_file.write(base_file.read())

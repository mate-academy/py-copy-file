def copy_file(command: str) -> None:
    command_str, old_file, new_file = command.split()

    if old_file != new_file and command_str == "cp":
        with (open(old_file, "r") as old_file,
              open(new_file, "w") as new_file):
            content = old_file.read()
            new_file.write(content)

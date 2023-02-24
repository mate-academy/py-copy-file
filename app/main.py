def copy_file(command: str) -> None:
    command_name, base_filename, new_filename = command.split()

    if base_filename != new_filename and command_name == "cp":
        with open(base_filename, "r") as inside, open(
                new_filename, "w"
        ) as outside:
            outside.write(inside.read())

def copy_file(command: str) -> None:
    command_list = command.split("")
    command_name, source_file, copied_file = command_list

    if len(command_list) != 3:
        return

    if command_name != "cp":
        return

    if source_file != copied_file:
        with (open(source_file, "r") as file,
              open(copied_file, "w") as copied_file):
            content = file.read()
            copied_file.write(content)

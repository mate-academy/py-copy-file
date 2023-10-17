def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) == 3 and command_list[0] == "cp":
        command_name, source_file, copied_file = command_list

        if source_file != copied_file:
            with (open(source_file, "r") as file,
                  open(copied_file, "w") as copied_file):
                content = file.read()
                copied_file.write(content)

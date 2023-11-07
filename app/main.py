def copy_file(command: str) -> None:
    command_content = command.split()
    if len(command_content) != 3:
        return

    cp_command, first_file, second_file = command_content

    if first_file == second_file or cp_command != "cp":
        return

    with (open(first_file, "r") as main_file,
          open(second_file, "w") as copied_file):
        copied_file.writelines(line for line in main_file)

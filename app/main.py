def copy_file(command: str) -> None:
    files_names = command.split()

    cp_command = files_names[0]
    first_file = files_names[1]
    second_file = files_names[2]

    if len(files_names) < 3 or first_file == second_file or cp_command != "cp":
        return

    with (open(files_names[1], "r") as main_file,
          open(files_names[2], "w") as copied_file):
        copied_file.writelines(line for line in main_file)

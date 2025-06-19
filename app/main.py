def copy_file(command: str) -> None:
    command_without_command = command.replace("cp", "")
    command_split_by_space = command_without_command.split(" ")
    files_names = [command_split_by_space[1], command_split_by_space[2]]

    with (open(files_names[1], "r") as file_in,
          open(files_names[2], "w") as file_out):
        file_out.writeLines(file_in.readlines())

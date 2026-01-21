def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3:
        command_name, source_filename, target_filename = command_split

        if command_name == "cp" and source_filename != target_filename:
            with (open(source_filename, "r") as file_in,
                  open(target_filename, "w") as file_out):
                file_out.write(file_in.read())

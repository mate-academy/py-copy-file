def copy_file(command: str) -> None:
    copy_command, source_file, target_file = command.split()
    if len(command) == 3:
        if "cp" == copy_command and source_file != target_file:
            with (
                open(source_file, "r") as file_in,
                open(target_file, "w") as file_out
            ):
                file_out.write(file_in.read())

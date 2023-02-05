def copy_file(command: str) -> None:
    command = command.split()
    copy_command = command[0]
    source_file = command[1]
    target_file = command[2]
    if len(command) == 3:
        if "cp" in copy_command and source_file != target_file:
            with open(f"{source_file}", "r") as file_in:
                with open(f"{target_file}", "w") as file_out:
                    file_out.write(file_in.read())

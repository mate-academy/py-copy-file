def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        action, file, new_file = command
        if action == "cp" and file != new_file:
            with (open(f"{file}", "r") as file_in,
                  open(f"{new_file}", "w") as file_out):
                file_out.write(file_in.read())

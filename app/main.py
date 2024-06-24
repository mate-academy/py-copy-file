def copy_file(command: str) -> None:
    splited_command = command.split(" ")
    action, file, new_file = splited_command

    if action == "cp" and len(splited_command) == 3:
        if file != new_file:
            with open(file) as file_in, open(new_file, "w") as file_out:
                file_out.write(file_in.read())

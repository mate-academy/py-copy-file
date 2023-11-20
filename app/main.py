def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if command == "cp" and old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            copy_content = file_in.read()
            file_out.write(copy_content)

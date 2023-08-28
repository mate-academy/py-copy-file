def copy_file(command: str) -> None:
    command, original_file, new_file = command.split()
    if command == "cp" and original_file != new_file:
        with open(original_file, "r") as file_in, \
             open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)

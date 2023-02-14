def copy_file(command: str) -> None:
    content = command.split()
    command, old_file, new_file = content[0], content[1], content[2]
    if command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            if old_file != new_file:
                content_to_copy = file_in.read()
                file_out.write(content_to_copy)

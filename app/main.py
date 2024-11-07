def copy_file(command: str) -> None:
    copy_command, old_file, new_file = command.split(" ")
    if copy_command == "cp" and old_file != new_file:
        with (open(old_file, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)

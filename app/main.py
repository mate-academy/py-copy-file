def copy_file(command: str) -> None:
    if "cp" in command:
        command_files = command.split()[1:]
        if len(set(command_files)) != 1:
            with (open(command_files[0], "r") as file,
                  open(command_files[1], "w") as f):
                text_to_copy = file.read()
                f.write(text_to_copy)

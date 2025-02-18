def copy_file(command_and_file_names: str) -> None:
    command, file_name, new_file_name = command_and_file_names.split(" ")
    if file_name != new_file_name:
        with (open(file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            content = old_file.read()
            new_file.write(content)

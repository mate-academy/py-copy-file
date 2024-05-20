def copy_file(command: str) -> None:
    old_file_name = command.split(" ")[1]
    new_file_name = command.split(" ")[2]
    if old_file_name == new_file_name:
        return
    with (open(old_file_name, "r") as old_file,
          open(new_file_name, "w") as new_file):
        text = old_file.read()
        new_file.write(text)

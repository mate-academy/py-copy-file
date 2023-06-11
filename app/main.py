def copy_file(command: str) -> None:
    if not command.startswith("cp ") or len(command.split(" ")) != 3:
        return
    old_file_name = command.split(" ")[1]
    new_file_name = command.split(" ")[2]
    if old_file_name == new_file_name:
        return
    with (open(old_file_name, "r") as old_file,
          open(new_file_name, "w") as new_file):
        new_file.write(old_file.read())

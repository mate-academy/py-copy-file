import os


def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command[0] != "copy":
        return
    _, old_file_name, new_file_name = command_split

    if old_file_name == new_file_name:
        return
    if not os.path.exists(old_file_name):
        print(f"Source file '{old_file_name}' does not exist.")
        return

    with (open(new_file_name, "r") as old_file,
          open(new_file_name, "w") as new_file):
        content = old_file.read()
        new_file.write(content)

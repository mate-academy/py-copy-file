import os


def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    if (command_parts[0] != "cp" or command_parts[1] == command_parts[2]):
        return
    if not os.path.exists(command_parts[1]):
        return
    with (open(command_parts[1], "r") as source_file,
          open(command_parts[2], "w") as target_file):
        content = source_file.read()
        target_file.write(content)

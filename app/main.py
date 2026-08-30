import os


def copy_file(command: str) -> None:
    new_command = command.split(" ")
    if len(new_command) != 3:
        return

    if "cp" != new_command[0]:
        return

    if new_command[1] == new_command[2]:
        return

    if not os.path.exists(new_command[1]):
        return

    with (open(new_command[1], "r") as file_in,
          open(new_command[2], "w") as file_out):
        new_file_content = file_in.read()
        file_out.write(new_file_content)

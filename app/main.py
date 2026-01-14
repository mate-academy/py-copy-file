# write your code here
def copy_file(command: str) -> None:
    cmd_parts = command.split()
    if len(cmd_parts) != 3 or cmd_parts[0] != "cp":
        return
    cp, file_name, new_file_name = cmd_parts
    if file_name == new_file_name:
        return
    try:
        with (open(file_name, "r") as file,
              open(new_file_name, "w") as new_file):
            content_to_copy = file.read()
            new_file.write(content_to_copy)
    except FileNotFoundError:
        return

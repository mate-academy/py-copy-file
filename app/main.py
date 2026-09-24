import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    com, f_name, s_name = parts
    if f_name == s_name or com != "cp" or not os.path.isfile(f_name):
        return
    with open(f_name, "r") as file_in, open(s_name, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

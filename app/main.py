import os


def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        return
    else:
        file_name = parts[1]
        new_file_name = parts[2]
    if (file_name == new_file_name
            or file_name not in os.listdir(".")) :
        return
    else:
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())

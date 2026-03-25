import os


def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) < 3:
        return

    action = parts[0]
    file_name1 = parts[1]
    file_name2 = parts[2]
    if (os.path.exists(file_name1)
            and action == "cp" and file_name2 != file_name1):
        with (open(file_name1, "r") as file_in,
              open(file_name2, "w") as file_out):
            file_out.write(file_in.read())

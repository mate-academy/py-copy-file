import os


def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3:
        return

    action = parts[0]
    file_source_name = parts[1]
    file_copy_name = parts[2]
    if (os.path.exists(file_source_name)
            and action == "cp" and file_copy_name != file_source_name):
        with (open(file_source_name, "r") as file_in,
              open(file_copy_name, "w") as file_out):
            file_out.write(file_in.read())

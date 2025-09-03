import os.path


def copy_file(command: str) -> None:
    file_names = command.split(" ")
    if len(file_names) != 3 or file_names[0] != "cp":
        return None
    file_in_name = file_names[1]
    file_out_name = file_names[2]
    if file_in_name == file_out_name or not os.path.exists(file_in_name):
        return None
    with (open(file_in_name, "r") as file_in,
          open(file_out_name, "w") as file_out):
        read_content = file_in.read()
        file_out.write(read_content)

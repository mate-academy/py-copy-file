

def copy_file(files_names: str) -> None:
    file_list = files_names.split(" ")
    if len(file_list) != 3 or file_list[0] != "cp":
        return

    _, source_file_name, destination_file_name = file_list

    if source_file_name == destination_file_name:
        return

    try:
        with (open(source_file_name, "r") as file_1,
              open(destination_file_name, "w") as file_2):
            data = file_1.read()
            file_2.write(data)
    except FileNotFoundError:
        return

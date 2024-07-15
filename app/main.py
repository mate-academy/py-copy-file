def copy_file(command: str) -> None:
    file_name_list = command.split()
    source_file = file_name_list[1]
    destination_file = file_name_list[2]
    if source_file == destination_file:
        return
    with (
        open(source_file, "r") as file_in,
        open(destination_file, "w") as file_out
    ):
        file_out.write(file_in.read())

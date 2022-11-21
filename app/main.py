def copy_file(command: str) -> None:
    list_with_info = command.split(" ")
    file_in_name = list_with_info[1]
    file_out_name = list_with_info[2]

    if file_in_name == file_out_name:
        return
    with (
        open(file_in_name, "r") as file_in,
        open(file_out_name, "w") as file_out
    ):
        file_out.write(file_in.read())
        file_in.close()
        file_out.close()

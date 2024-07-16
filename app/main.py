def copy_file(command: str) -> None:
    file_name_list = command.split()
    if len(file_name_list) != 3 or file_name_list[0] != "cp":
        print("Invalid command")
        return
    source_file, destination_file = file_name_list[1:]
    if source_file == destination_file:
        return
    with (
        open(source_file, "r") as file_in,
        open(destination_file, "w") as file_out
    ):
        file_out.write(file_in.read())

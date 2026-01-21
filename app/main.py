def copy_file(command: str) -> None:
    try:
        destination_file_name = command.split()
        if destination_file_name[0] != "cp":
            return
        if len(destination_file_name) != 3:
            return
        if destination_file_name[1] == destination_file_name[2]:
            return


        with open(destination_file_name[1], "r") as file_in, \
                open(destination_file_name[2], "w") as file_out:
            file_out.write(file_in.read())

    except (FileNotFoundError, IndexError):
        return

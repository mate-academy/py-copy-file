def copy_file(command: str) -> None:
    my_command, existed_file, file_to_create = command.split()
    if existed_file != file_to_create and my_command == "cp":
        with open(existed_file, "r") as file_in, open(
            file_to_create, "w"
        ) as file_out:
            file_out.write(file_in.read())

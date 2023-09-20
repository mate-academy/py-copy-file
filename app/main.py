def copy_file(command: str) -> None:
    command = command.split()
    start_command, origin_file, new_file = command[0], command[1], command[2]
    if origin_file != new_file and start_command == "cp":
        with (open(origin_file, "r") as file_in,
                open(new_file, "w") as file_out):
            file_out.write(file_in.read())

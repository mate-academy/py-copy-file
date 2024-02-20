def copy_file(command: str) -> None:
    command_cp, origin_file, copy_file, *_ = command.split()

    if origin_file != copy_file and command_cp == "cp":
        with (open(copy_file, "w") as file_for_write,
              open(origin_file, "r") as origin_data):
            file_for_write.write(origin_data)

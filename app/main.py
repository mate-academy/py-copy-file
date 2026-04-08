def copy_file(command: str) -> None:

    source_file_name = command.split()

    if len(source_file_name) != 3 or source_file_name[0] != "cp":
        return

    if source_file_name[1] == source_file_name[2]:
        return
    else:
        try:
            with open(source_file_name[1], "r") as file_in:
                with open(source_file_name[2], "w") as file_out:
                    file_out.write(file_in.read())
        except OSError:
            return

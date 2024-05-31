def copy_file(command: str) -> None:
    parts = command.split()

    if parts[0] == "cp":
        source_file_name, copy_file_name = parts[1], parts[2]
        if source_file_name != copy_file_name:
            try:
                with open(source_file_name, "r") as file_in, \
                        open(copy_file_name, "w") as file_out:
                    for line in file_in:
                        file_out.write(line)
            except FileNotFoundError:
                pass
            except IOError:
                pass

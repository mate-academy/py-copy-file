def copy_file(command: str) -> None:
    components = command.split()
    if len(components) == 3:
        cmd, source_path, destination_path = components
        if source_path != destination_path and cmd == "cp":
            with open(source_path, "r") as file_in, \
                    open(destination_path, "w") as file_out:
                file_out.write(file_in.read())
    return

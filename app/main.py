def copy_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    destination_file = parts[2]
    if (len(parts) == 3 and parts[0] == "cp"
            and source_file != destination_file):
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    return

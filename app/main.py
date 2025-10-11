def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) == 3 and parts[0] == "cp":
        source_file_name, destination_file_name = parts[1], parts[2]
        if source_file_name != destination_file_name:
            with (open(source_file_name) as copied_file,
                  open(destination_file_name, "w") as pasted_file):
                pasted_file.write(copied_file.read())

def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp" and parts[1] != parts[2]:
        source_file_name, target_file_name = parts[1], parts[2]
        try:
            with (open(source_file_name, "r") as source_file,
                  open(target_file_name, "w") as target_file):
                target_file.write(source_file.read())
        except FileNotFoundError:
            pass

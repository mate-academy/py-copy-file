def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        old_file, new_file = parts[1], parts[2]
        if parts[1] != parts[2]:
            try:
                with open(old_file, "r") as sourse_file:
                    with open(new_file, "w") as dest_file:
                        for line in sourse_file:
                            dest_file.write(line)
            except (FileNotFoundError):
                pass

def copy_file(command: str) -> None:
    files_names = command.split(" ")
    if files_names[0] == "cp":
        if len(files_names) == 3:
            if files_names[1] != files_names[2]:
                try:
                    with (
                        open(files_names[1], "r") as old_file,
                        open(files_names[2], "w") as new_file
                    ):
                        new_file.write(old_file.read())
                except Exception:
                    return
    return

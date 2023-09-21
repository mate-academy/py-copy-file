def copy_file(command: str) -> None:
    files_names = command.split()
    if len(files_names) == 3:
        if files_names[0] == "cp" and files_names[1] != files_names[2]:
            with (
                open(files_names[1], "r") as file_in,
                open(files_names[2], "w") as file_out
            ):
                if files_names[1] != files_names[2]:
                    original_file = file_in.read()
                    file_out.write(original_file)

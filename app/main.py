def copy_file(command: str) -> None:
    cmd, file_original, file_copy = command.split(" ")
    if cmd == "cp" and file_original != file_copy:
        with open(file_original, "r") as file_in, open(
            file_copy, "w"
        ) as file_out:
            for line in file_in:
                file_out.write(line)

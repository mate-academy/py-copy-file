def copy_file(command: str) -> None:
    split_command = command.split()
    cp_cmd, file_in, file_out = split_command
    if len(split_command) == 3:
        if cp_cmd == "cp" and file_in != file_out:
            with (open(file_in, "r") as source_file,
                  open(file_out, "w") as end_file):
                end_file.write(source_file.read())

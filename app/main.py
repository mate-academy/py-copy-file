def copy_file(command: str) -> None:
    cmd, file_org, file_copy = command.split()

    if cmd == "cp" and file_org != file_copy:
        with open(file_org, "r") as file_out, open(file_copy, "w") as file_in:
            file_in.write(file_out.read())

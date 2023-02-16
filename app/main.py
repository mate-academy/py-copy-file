def copy_file(command: str) -> None:
    file_org = command.split()[1]
    file_copy = command.split()[2]

    if command.startswith("cp") and file_org != file_copy:
        with open(file_org, "r") as file_out, open(file_copy, "w") as file_in:
            file_in.write(file_out.read())

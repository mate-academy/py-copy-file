def copy_file(command: str) -> None:
    files_names = command.split()
    if files_names[1] == files_names[2]:
        return
    with open(f"{files_names[1]}", "r") as file_in, \
            open(f"{files_names[2]}", "w") as file_out:
        content = file_in.read()
        file_out.write(content)

def copy_file(command: str) -> str:
    source = command.split()[1]
    copy = command.split()[2]

    if source != copy:
        with open(source, "r") as file_in:
            with open(copy, "w") as file_out:
                file_out.write(file_in.read())

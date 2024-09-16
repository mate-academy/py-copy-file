def copy_file(command: str) -> None:
    elements = command.split()
    if len(elements) == 3:
        command, file_in, file_out = elements
        if command == "cp" and file_in != file_out:
            with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
                f_out.write(f_in.read())

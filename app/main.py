def copy_file(command: str) -> None:
    file_in, file_out = command.split()[1:]

    if file_in != file_out:
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            content = file_in.read()
            file_out.write(content)

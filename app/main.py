def copy_file(command: str) -> None:
    file_operation, file_in, file_out = command.split()

    if file_in != file_out and file_operation == "cp":
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            content = file_in.read()
            file_out.write(content)

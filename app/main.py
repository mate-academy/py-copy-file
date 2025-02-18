def copy_file(command: str) -> None:
    command, file_in, file_out = command.split()
    if command != "cp":
        print("Invalid command")
        return
    if file_in != file_out:
        with open(file_in, "r") as file_in, open(file_out, "a") as file_out:
            file_out.write(file_in.read())

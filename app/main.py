def copy_file(command: str) -> None:
    if command[:2] == "cp":
        command = command.split(" ")
        file_in = command[1]
        file_out = command[2]
        if file_in != file_out:
            with open(file_in, "r") as f_in:
                f_out = open(file_out, "w")
                f_out.write(f_in.read())

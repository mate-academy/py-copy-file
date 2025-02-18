def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        cmd, file1, file2 = command.split()
        if file1 != file2 and cmd == "cp":
            with open(file1, "r") as file_in, open(file2, "w") as file_out:
                file_out.write(file_in.read())

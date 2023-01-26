def copy_file(command: str) -> None:
    result = command.split()
    if result[0] == "cp":
        if result[1] != result[2]:
            with open(result[1], "r") as file_in,\
                 open(result[2], "w") as file_out:
                file_out.write(file_in.read())

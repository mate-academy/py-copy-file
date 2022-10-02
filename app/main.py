def copy_file(command: str):
    file = command.split(" ")
    if file[0] == "cp":
        if file[1] != file[2]:
            with open(file[1], "r") as file_in, open(file[2], "w") as file_out:
                for line in file_in:
                    file_out.write(line)

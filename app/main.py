def copy_file(command: str) -> None:
    c_list = command.split()
    if len(c_list) == 3 and c_list[0] == "cp":
        if c_list[1] != c_list[2]:
            with open(c_list[1], "r") as file_in, open(c_list[2], "w") as file_out:
                file_out.write(file_in.read())
            file_in.close()
            file_out.close()
        else:
            pass

def copy_file(command: str) -> None:
    # cp file.txt file-copy.txt
    if len(command.split()) != 3 or command[:3] != "cp ":
        return 0
    name_f_in = command.split()[1]
    name_f_out = command.split()[2]
    if name_f_in == name_f_out:
        return 0
    with open(name_f_in, "r") as file_in, open(name_f_out, "w") as file_out:
        file_out.write(file_in.read())

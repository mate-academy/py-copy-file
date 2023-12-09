def copy_file(command: str) -> None:
    command = command.split(" ")
    try:
        main_command = str(command[0])
        if main_command == "cp":
            f_in = str(command[1])
            f_out = str(command[2])
    except IndexError:
        pass

    with open(f_in, "r") as file_in, open(f_out, "w") as file_out:
        if f_in != f_out:
            tmp = file_in.read()
            file_out.write(tmp)

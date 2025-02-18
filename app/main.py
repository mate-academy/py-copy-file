def copy_file(command: str) -> None:
    command_list = command.split(" ")
    cp = command_list[0]
    f_in = command_list[1]
    f_out = command_list[2]
    if len(command_list) == 3 and cp == "cp":
        try:
            if f_in == f_out:
                return None
            with open(f_in, "r") as file_in, open(f_out, "w") as file_out:
                info = file_in.read()
                file_out.write(info)
        except FileNotFoundError:
            print(f"Error: File '{f_in}' not found.")

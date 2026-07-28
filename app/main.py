def copy_file(command: str) -> None:
    try:
        list_command = command.split(" ")
        if list_command[0] != "cp":
            return
        if len(list_command) < 3:
            return
        if list_command[1] == list_command[2]:
            return
        with (open(list_command[1], "r+") as file_in,
              open(list_command[2], "w") as file_out
              ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"invalid command: {command}")

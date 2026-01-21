def copy_file(command: str) -> None:
    command_lst = command.split()
    if len(command_lst) != 3:
        print("You must give argument in format "
              "(command, file name, new file for copy)")
        return
    if command_lst[0] != "cp":
        print("command must be 'CP'")
        return
    if command_lst[1] != command_lst[2]:
        try:
            with (open(command_lst[1], "rb") as f,
                  open(command_lst[2], "wb") as f_copy):
                for line in f.readlines():
                    f_copy.write(line)
        except FileNotFoundError as e:
            print(f"{e}")
    return

def copy_file(command: str) -> None:
    if not isinstance(command, str) or len(command) <= 1:
        print("Command is incorrect")
        return

    if command[:2] != "cp":
        print("Command should start with 'cp'")
        return

    cmd_list = command.strip().split(" ")
    if len(cmd_list) <= 2:
        print("Command 'cp' should contains at least two arguments")
        return

    if cmd_list[-2] == cmd_list[-1]:
        print("Warning: arguments are the same")
        return

    try:
        open(cmd_list[-1], "r")
    except FileNotFoundError:
        pass
    else:
        confirm = input("Destination file exists, confirm override (y/n):")
        while confirm not in ["y", "Y", "n", "N"]:
            confirm = input("Destination file exists, confirm override (y/n):")
        if confirm in ["n", "N"]:
            return

    with open(cmd_list[-2], "r") as file_in,\
            open(cmd_list[-1], "w") as file_out:
        for line in file_in.readlines():
            file_out.write(line)

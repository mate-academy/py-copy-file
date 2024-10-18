def copy_file(command: str) -> None:
    if not isinstance(command, str):
        print("Incorrect format")
        return

    cmd_list = command.strip().split(" ")

    if len(cmd_list) and cmd_list[0] != "cp":
        print("Command should be 'cp'")
        return

    if len(cmd_list) <= 2:
        print("Command 'cp' should contains at least two arguments")
        return

    source_name = cmd_list[-2]
    destination_name = cmd_list[-1]

    if source_name == destination_name:
        print("Warning: arguments are the same")
        return

    try:
        open(source_name, "r")
    except FileNotFoundError:
        print("Warning: source file doesn't exist")
        return

    try:
        open(destination_name, "r")
    except FileNotFoundError:
        pass
    else:
        confirm = input("Destination file exists, confirm override (y/n):")
        while confirm not in ["y", "Y", "n", "N"]:
            confirm = input("Destination file exists, confirm override (y/n):")
        if confirm in ["n", "N"]:
            return

    with open(source_name, "r") as source_file,\
            open(destination_name, "w") as destination_file:
        for line in source_file.readlines():
            destination_file.write(line)

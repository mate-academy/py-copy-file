def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        print("Invalid command. Command should have three arguments.")
        return
    f_list = command.split()
    if f_list[1] == f_list[2]:
        return
    with open(f_list[1], "r") as f_out, open(f_list[2], "w") as f_in:
        f_in.write(f_out.read())

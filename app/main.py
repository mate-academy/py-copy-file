def copy_file(command: str) -> None:
    lst = command.split()
    if lst[0] == "cp":
        if lst[1] != lst[2]:
            with open(lst[1], "r") as file_in, open(lst[2], "w") as file_out:
                file_out.write(file_in.read())

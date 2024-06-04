def copy_fil(command: str) -> None:
    lst = command.split()
    from_file = lst[0]
    to_file = lst[1]

    if from_file != to_file:
        with open(from_file, "r") as file_out, open(to_file, "a") as file_in:
            file_in.write(file_out.read())

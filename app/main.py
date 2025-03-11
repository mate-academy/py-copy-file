def copy_file(command: str) -> None:
    lis = command.split()
    if len(lis) < 3 or lis[1] == lis[2] or lis[0] != "cp":
        return None
    try:
        with open(lis[1], "r") as file_in, open(lis[2], "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except Exception as e:
        return e

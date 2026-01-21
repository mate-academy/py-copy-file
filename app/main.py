def copy_file(command: str) -> None:
    params = command.split()
    if len(params) != 3 or params[0] != "cp" or params[1] == params[2]:
        return
    try:
        file1 = open(params[1], "r")
    except FileNotFoundError as e:
        print(e)
        return
    content = file1.read()
    file1.close()
    file2 = open(params[2], "w")
    file2.write(content)
    file2.close()

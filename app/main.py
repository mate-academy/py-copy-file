def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        raise Exception("this interface support only 'cp' command")
    ls_with_name = command.split()[1:]
    if ls_with_name[0] != ls_with_name[1]:
        with open(ls_with_name[0], "r") as file1,\
                open(ls_with_name[1], "w") as file2:
            file2.write(file1.read())

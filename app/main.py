def copy_file(command: str) -> None:
    list_file = command.split()
    if list_file == 3 and list_file[1] != list_file[2]:
        with open(list_file[1], "r") as f, open(list_file[2], "w") as g:
            g.write(f.read())

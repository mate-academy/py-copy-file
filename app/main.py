
def copy_file(command: str) -> None:
    comm = command.split()
    if len(comm) == 3:
        if comm[0] == "cp" and comm[1] != comm[2]:
            try:
                with (open(comm[1], "r") as read_file,
                      open(comm[2], "w") as write_file
                      ):
                    text = read_file.read()
                    write_file.write(text)
            except FileNotFoundError:
                return
        else:
            return

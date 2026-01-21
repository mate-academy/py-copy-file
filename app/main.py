def copy_file(command: str) -> None:
    if (len(command.split(" ")) != 3 or command.split(" ")[0] != "cp"
            or command.split(" ")[1] == command.split(" ")[2]):
        return
    else:
        try:
            cp, file, new_file = command.split(" ")
            with open(file, "r") as f1, open(new_file, "w") as f2:
                for line in f1.read():
                    f2.write(line)
        except FileNotFoundError:
            pass

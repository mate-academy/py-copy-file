def copy_file(comand: str) -> None:
    names = comand.split()
    if names[0] == "cp" and names[1] != names[2]:
        with open(names[1], "r") as file_in, open(names[2], "w") as file_out:
            file_out.write(file_in.read())

def copy_file(command: str) -> None:
    name = command.split(" ")

    if len(name) == 3 and name[0] == "cp" and not name[1] == name[2]:

        with open(name[1], "r") as file_in:
            text = file_in.read()

        with open(name[2], "w") as file_out:
            file_out.write(text)

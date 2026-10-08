def copy_file(command: str) -> None:

    splitted = command.split(" ")

    if splitted[0] != "cp":
        return
    if len(splitted) < 3:
        return
    if splitted[1] == splitted[2]:
        return
    try :
        open(splitted[1])
    except FileNotFoundError:
        return
    else:
        with open(splitted[1]) as file_in , open(splitted[2], "w") as file_out:
            content = file_in.read()
            file_out.write(content)

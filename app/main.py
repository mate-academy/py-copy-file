def copy_file(command: str) -> None:

    splitted = command.split(" ")

    if splitted[0] != "cp":
        return
    paths = [path for path in splitted if path.endswith(".txt")]
    if len(paths) < 2:
        return
    if paths[0] == paths[1]:
        return

    try :
        open(paths[0])
    except FileNotFoundError:
        return
    else:
        with open(paths[0]) as file_in , open(paths[1], "w") as file_out:
            content = file_in.read()
            file_out.write(content)

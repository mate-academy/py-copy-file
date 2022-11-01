def copy_file(command: str) -> None:

    file, new_file = command.split()[1:]

    if file == new_file:
        print("Nothing changed")
        return
    else:
        with open(file, "r") as inp, open(new_file, "w") as out:
            out.write(inp.read())


def copy_file(command: str) -> None:
    nod = command.strip().split()

    if nod[0] != "cp" or nod[1] == nod[2]:
        return
    try:
        with open(nod[1], "r") as file_in:
            content = file_in.read()
        with open(nod[2], "w") as file_out:
            file_out.write(content)
    except FileNotFoundError:
        print(f"File {nod[1]} not found.")

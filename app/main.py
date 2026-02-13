def copy_file(command: str) -> None:
    if len(command) == 0:
        return
    try:
        nowa = command[3:]
    except IndexError:
        return
    lista = nowa.split()
    try:
        file1 = lista[0]
        file2 = lista[1]
    except IndexError:
        return
    if file1 == file2:
        return
    try:
        plik = open(file1, "r")
        content = plik.read()
    except FileNotFoundError:
        return
    plik1 = open(file2, "w")
    plik1.write(content)
    plik.close()
    plik1.close()

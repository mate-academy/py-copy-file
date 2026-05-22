def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3:
        return

    if parts[0] != "cp":
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    try:
        with open(source, "r") as r:
            conteudo = r.read()

        with open(destination, "w") as f:
            f.write(conteudo)

    except FileNotFoundError:
        return

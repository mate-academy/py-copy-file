def copy_file(command: str) -> None:

    if len(command.split()) == 3 and command.split()[0] == "cp":
        arquivo_original = command.split()[1]
        arquivo_novo = command.split()[2]
        if arquivo_original == arquivo_novo:
            return

        try:
            with (open(arquivo_original, "r") as f1,
                  open(arquivo_novo, "w") as f2):
                f2.write(f1.read())
        except FileNotFoundError:
            return

from pathlib import Path


def copy_file(command: str) -> None:
    parts = command.split()

    # Verifica se o comando tem o formato correto e se inicia com "cp"
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts

    # Não faz nada se o arquivo de origem e o de destino forem iguais
    if source == destination:
        return

    # Verifica se o arquivo de origem existe antes de tentar abrir
    if not Path(source).is_file():
        return

    with open(source, "r", encoding="utf-8") as file_in, \
            open(destination, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())

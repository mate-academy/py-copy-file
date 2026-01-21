def copy_file(command: str) -> None:
    parts = command.strip().split()

    # Verifica se o comando tem exatamente 3 partes e começa com 'cp'
    if len(parts) != 3 or parts[0] != "cp":
        return

    source, destination = parts[1], parts[2]

    # Não faz nada se os nomes forem iguais
    if source == destination:
        return

    try:
        # Copia o conteúdo do arquivo
        with (
            open(source, "r", encoding="utf-8") as file_in,
            open(destination, "w", encoding="utf-8") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        # Silenciosamente ignora se o arquivo de origem não existe
        pass

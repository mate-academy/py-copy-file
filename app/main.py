import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    file_in_name = parts[1]
    file_out_name = parts[2]

    # Verifica se o arquivo de origem existe e se os nomes são diferentes
    if file_in_name == file_out_name or not os.path.exists(file_in_name):
        return

    with open(file_in_name, "r") as file_in, \
            open(file_out_name, "w") as file_out:
        file_out.write(file_in.read())

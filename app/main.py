import os


def copy_file(command: str) -> None:
    lista = command.split(" ")
    if len(lista) != 3 or lista[0] != "cp":
        return
    file_to_copy = lista[1]
    file_to_save = lista[2]
    if file_to_copy == file_to_save:
        return
    if not os.path.exists(file_to_copy):
        return

    with (open(file_to_copy, "r") as file_in,
          open(file_to_save, "w") as file_out):
        file_out.write(file_in.read())

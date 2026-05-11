import os


def copy_file(command: str) -> None:
    data = command.split(" ")
    if len(data) != 3 or data[0] != "cp":
        return
    if data[1] == data[2]:
        return

    source, destination = data[1], data[2]
    if source == destination:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write((file_in.read()))

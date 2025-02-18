def copy_file(command: str) -> None:
    source, destination = command.split(" ", 1)
    if source == destination:
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        data = file_in.read()
        file_out.write(data)

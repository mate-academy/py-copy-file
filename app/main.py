def copy_file(command: str) -> None:
    cp, source, destination = command.split(" ")
    if source == destination or cp != "cp":
        return
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        text_to_copy = file_in.read()
        file_out.write(text_to_copy)

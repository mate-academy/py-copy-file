def copy_file(command: str) -> None:
    command, incoming_file_path, outgoing_file_path = command.split(" ")
    if incoming_file_path == outgoing_file_path or command != "cp":
        return

    with (
        open(incoming_file_path, "r") as incoming_file,
        open(outgoing_file_path, "w") as outgoing_file
    ):
        outgoing_file.write(incoming_file.read())

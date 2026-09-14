def copy_file(command: str) -> None:
    try:
        action, source, destination = command.split()

        if action != "cp":
            return

        if source == destination:
            return

        with open(source, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except Exception:
        return

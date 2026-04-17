def copy_file(command: str) -> str:
    parts = command.split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        cp, source, destination = parts
        if source != destination:
            try:
                with open(source, "r") as file_in, \
                        open(destination, "w") as file_out:
                    file_out.write(file_in.read())
            except FileNotFoundError:
                pass

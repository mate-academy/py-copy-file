def copy_file(command: str) -> None:
    separated = command.split()
    if len(separated) == 3:
        order = separated[0]
        source = separated[1]
        destination = separated[2]
        if order == "cp":
            if source == destination:
                return
            try:
                with (
                    open(source, "r") as opened,
                    open(destination, "w") as written
                ):
                    moved = opened.read()
                    written.write(moved)
            except FileNotFoundError:
                return

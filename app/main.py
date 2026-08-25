def copy_file(command: str) -> None:
    split_com = command.split()
    if len(split_com) == 3:
        order = split_com[0]
        source = split_com[1]
        destination = split_com[2]
        if order == "cp":
            if source == destination:
                return
            try:
                with (
                    open(source, "r") as file_in,
                    open(destination, "w") as file_out
                ):
                    moved = file_in.read()
                    file_out.write(moved)
            except FileNotFoundError:
                return

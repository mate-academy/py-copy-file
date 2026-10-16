def copy_file(command: str) -> None:

    list_str = command.split(" ")
    if len(list_str) != 3:
        return
    if list_str[0] == "cp":
        source = list_str[1]
        destination = list_str[2]
        if source == destination:
            return
        try:
            with (open(source, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            return

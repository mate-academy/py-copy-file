def copy_file(command: str) -> None:
    strings = command.split()
    cp = ""
    name_copy = ""
    name_origin = ""

    if len(strings) == 3:
        cp, name_origin, name_copy = strings
    if name_origin != name_copy and cp == "cp":
        try:
            with (open(name_origin, "rb") as file_origin,
                  open(name_copy, "wb") as file_copy):
                for line in file_origin:
                    file_copy.write(line)
                # file_copy.write(file_origin.read())
        except FileNotFoundError:
            print("File not found")

def copy_file(command: str) -> None:

    if command == "":
        return None

    part = command.split(" ")

    if len(part) != 3:
        return None

    if part[1] != part[2] and part[0] == "cp" and len(part) == 3:
        try:
            with open(part[1], "r") as file_in, open(part[2], "w") as file_out:
                for line in file_in.readlines():
                    file_out.write(line)
        except FileNotFoundError:
            return None

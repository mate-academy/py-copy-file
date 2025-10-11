def copy_file(command: str) -> None:
    parts = command.strip().split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        if parts[1] != parts[2]:
            try:
                with open(parts[1]) as copied_file:
                    content = copied_file.read()
                with open(parts[2], "w") as pasted_file:
                    pasted_file.write(content)
            except FileNotFoundError:
                """"""

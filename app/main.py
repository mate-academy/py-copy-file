def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        if parts[1] == parts[2]:
            return
        try:
            with open(parts[1], "r") as file1, open(parts[2], "w") as file2:
                content = file1.read()
                file2.write(content)

        except FileNotFoundError:
            pass

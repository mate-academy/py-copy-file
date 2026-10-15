def copy_file(command: str) -> None:
    enter = command.split()
    if len(enter) < 3 or len(enter) > 3 or enter[1] == enter[2]:
        return

    try:
        if enter[0] == "cp":
            with open(enter[1], "r") as file_read:
                text_file = file_read.read()
            with open(enter[2], "w") as file_write:
                file_write.write(text_file)
    except FileNotFoundError:
        pass

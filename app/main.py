def copy_file(command: str) -> None:
    text = command.split(" ")
    if text[0] == "cp":
        if text[1] != text[2]:
            with open(text[1], "r") as file_in, open(text[2], "w") as file_out:
                file_out.write(file_in.read())

def copy_file(command: str) -> None:
    words = command.split(" ")
    if len(words) != 3 or words[0] != "cp":
        return None
    if words[1] != words[2]:
        with open(words[1], "r") as file_in, open(words[2], "w") as file_out:
            file_out.write(file_in.read())

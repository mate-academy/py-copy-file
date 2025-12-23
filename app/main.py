def copy_file(command: str) -> None:
    words = command.split()
    if (len(words) == 3) and (words[0] == "cp") and (words[1] != words[2]):
        try:
            with (open(words[1], "r") as file_in,
                  open(words[2], "w") as file_copy):
                file_copy.write(file_in.read())
        except FileNotFoundError:
            return

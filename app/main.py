def copy_file(command: str) -> None:
    ls = command.split()
    if len(ls) == 3 and ls[0] == "cp" and ls[1] != ls[2]:
        with open(ls[1], "r") as file_in, open(ls[2], "w") as file_out:
            file_out.write(file_in.read())
    else:
        print("command should be in this format <cp file.txt new_file.txt>")

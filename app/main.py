def copy_file(command: str) -> None:
    words = command.split()
    print(words[1])
    print(words[2])
    if words[0] == "cp" and words[1] != words[2]:
        with open(words[1], "r") as file_in, open(words[2], "w") as file_out:
            context = file_in.read()
            file_out.write(context)
    else:
        pass

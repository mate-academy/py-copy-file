def copy_file(string: str):
    words = string.split()
    if words[1] != words[2]:
        with open(words[1], "r") as file_in, open(words[2], "w") as file_out:
            copy = file_in.read()
            file_out.write(copy)

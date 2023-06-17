def copy_file(command: str) -> None:
    words = command.split(" ")
    if words[1] != words[2]:
        with open(words[1], "r") as file_in, open(words[2], "w") as file_out:
            file_out.write(file_in.read())


copy_file("cp fl.txt fl_copy.txt")
copy_file("cp fl_copy.txt fl_copy1.txt")

print(
    open("fl.txt").read() == open("fl_copy.txt").read()
)

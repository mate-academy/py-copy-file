def copy_file(command: str) -> bool:
    cp_file = command.split(" ")[1]
    new_file = command.split(" ")[2]

    if cp_file != new_file:
        with (open(cp_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
            return open("file.txt").read() == open("new_file.txt").read()


copy_file("cp file.txt file.txt")
copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())

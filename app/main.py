def copy_file(command: str) -> None:
    file_origin = command.split()[1]
    cp_file = command.split()[2]
    if file_origin != cp_file:
        with open(file_origin, "r") as file_in, open(cp_file, "w") as file_out:
            file_out.write(file_in.read())


file = open("file.txt", "w")
file.write("Hallo world!!!")
file.close()


copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())
print(open("file.txt").read())
print(open("new_file.txt").read())

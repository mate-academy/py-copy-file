def copy_file(command: str):
    new_file = command.split(" ")
    new_file.remove(new_file[0])
    with open(new_file[1], "r") as file_in, open(new_file[2], "w") as file_out:
        for info in file_in:
            file_out.write(info)


copy_file("cp file.txt new_file.txt")

# write your code here


def copy_file(command: str) -> None:
    _, src_file, dest_file = command.split()
    if src_file != dest_file:
        with open(src_file, "r") as file_in, open(dest_file, "w") as file_out:
            file_out.write(file_in.read())


print(copy_file("cp file.txt new_file.txt"))

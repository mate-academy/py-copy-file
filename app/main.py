def copy_file(command: str) -> None:
    f_name = command.split()
    if f_name[1] != f_name[2]:
        with open(f_name[1], "r") as file_in, open(f_name[2], "w") as file_out:
            file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp test1.txt test2.txt")

def copy_file(command: str) -> None:
    cmd, file1, file2 = command.split(" ")

    if file1 == file2:
        return

    if cmd == "cp":
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp filename.txt filename_new.txt")

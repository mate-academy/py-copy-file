def copy_file(command: str) -> None:
    file_name = command.split(" ")

    if (
        file_name[0] != "cp"
        or len(file_name) != 3
        or file_name[1] == file_name[2]
    ):
        return

    with (
        open(file_name[1], "r") as file_in,
        open(file_name[2], "w") as file_out
    ):
        file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
    print(open("file.txt").read() == open("new_file.txt").read())

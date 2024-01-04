def copy_file(command: str) -> None:
    way = command.split()

    if len(way) == 3 and way[1] != way[2]:
        with (open(way[1], "r") as file_in,
              open(way[2], "w") as file_out):
            file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
    # open("file.txt").read() == open("new_file.txt").read()

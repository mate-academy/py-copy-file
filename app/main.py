def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()

    if old_file == new_file or command != "cp":
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")

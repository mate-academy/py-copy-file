def copy_file(command: str) -> None:
    command = command.split()
    if command[1] != command[2]:
        with open(command[1], "r") as file, open(command[2], "w") as file_copy:
            content = file.read()
            file_copy.write(content)


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")

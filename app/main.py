def copy_file(command: str) -> None:
    listed_command = command.split()
    first_file = listed_command[1]
    second_file = listed_command[2]
    if first_file != second_file:
        with open(first_file, "r") as f, \
                open(second_file, "w") as s:
            text_to_copy = str(f.read())
            s.write(text_to_copy)


if __name__ == "__main__":
    copy_file("cp text.txt new_file.txt")

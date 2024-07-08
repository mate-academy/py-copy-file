def copy_file(command: str) -> None:
    command, first_file, second_file = command.split()
    if command == "cp" and first_file != second_file:
        with (open(first_file, "r") as file,
              open(second_file, "w") as file_copy):
            content = file.read()
            file_copy.write(content)


if __name__ == "__main__":
    copy_file("cp file.txt file22.txt")

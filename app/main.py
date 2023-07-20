def copy_file(command: str) -> None:
    command_name, file_name, new_name = command.split(" ")
    if (command_name == "cp"
            and new_name != file_name):
        with open(f"{file_name}") as file:
            content = file.read()
        with open(f"{new_name}", "w") as new_file:
            new_file.write(content)


if __name__ == "__main__":
    file_one = "file.txt"
    file_two = "new_file.txt"
    copy_file(f"cp {file_one} {file_two}")
    with open(file_one) as one, open(file_two) as two:
        print(one.read() == two.read())

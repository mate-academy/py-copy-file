def copy_file(command: str) -> None:
    content = command.split(" ")
    if content[1] != content[2]:
        file_one = content[1]
        file_two = content[2]
        with open(file_one, "r") as file_in, open(file_two, "w") as file_out:
            file_out.write(file_in.read())

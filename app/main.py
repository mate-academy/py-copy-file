def copy_file(command: str) -> None:
    temp = command.split(" ")
    if temp[1] == temp[2]:
        return
    with open(temp[1], "r") as file_in, open(temp[2], "w") as file_out:
        content = file_in.read()
        file_out.write(content)

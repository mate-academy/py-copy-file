def copy_file(command: str) -> None | bool:
    command = command.split(" ")[1:]
    if command[0] != command[1]:
        with (open(command[0], "r") as file_in,
              open(command[1], "w") as file_out):
            file_out.write(file_in.read())
        if open("file.txt").read() == open("new_file.txt").read():
            return True
    return

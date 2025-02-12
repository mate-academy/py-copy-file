def copy_file(command: str) -> None:
    command = command.split(" ")

    if command[0] == "cp" and command[1] != command[2]:
        with (open(command[1], "r") as file_in,
              open(command[2], "w") as file_out):
            for content in file_in.readlines():
                file_out.write(content)

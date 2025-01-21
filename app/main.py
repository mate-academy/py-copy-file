def copy_file(command: str) -> None:
    command_split = command.split(" ")
    while True:
        if command_split[0] != "cp" or len(command_split) != 3:
            break
        if command_split[1] == command_split[2]:
            break

        with (open(command_split[1], "r") as file_in,
              open(command_split[2], "w") as file_out):
            file_out.write(file_in.read())
        break


if __name__ == "__main__":
    copy_file()

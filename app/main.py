def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if (command_split[0] == "cp"
            and len(command_split) == 3
            and command_split[1] != command_split[2]):
        with (open(command_split[1], "r") as file_in,
              open(command_split[2], "w") as file_out):
            file_out.write(file_in.read())


if __name__ == "__main__":
    command = str(input())
    copy_file(command)

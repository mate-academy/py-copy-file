def copy_file(command: str) -> None:
    command_split = command.split()
    if command_split[0] != "cp":
        print("There is no such command")
        return

    if command_split[1] == command_split[2]:
        return

    print(command_split[1])
    with (open(command_split[1], "r") as file_in,
          open(command_split[2], "w") as file_out):
        content = file_in.read()
        file_out.write(content)
    print(command_split)

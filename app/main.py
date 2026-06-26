def copy_file(command: str) -> None:
    com_split = command.split()
    if len(com_split) < 3 or com_split[0] != "cp":
        print(f"Invalid command: {command}")
        return
    if com_split[1] != com_split[2]:
        try:
            with open(com_split[1], "r") as file_in, open(
                com_split[2], "w"
            ) as file_out:
                content = file_in.read()
                file_out.write(content)
        except FileNotFoundError as e:
            print(f"Error: {e}")

def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if (len(split_command) < 3
            or split_command[0] != "cp"
            or split_command[1] == split_command[2]):
        return
    try:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: The file '{split_command[1]}' does not exist.")

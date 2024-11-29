def copy_file(command: str) -> None:
    split_command = command.split(" ")

    if (len(split_command) == 3
            and split_command[0] == "cp"
            and split_command[1] != split_command[2]):

        with (open(f"{split_command[1]}", "r") as file_in,
              open(f"{split_command[2]}", "w+") as file_out):
            file_out.write(file_in.read())

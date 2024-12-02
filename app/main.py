def copy_file(command: str) -> None:
    split_command = command.split(" ")
    action, source, destination = split_command
    if (len(split_command) != 3
            and action != "cp"
            and source == destination):
        raise ValueError("Wrong command was entered!")

    with (open(f"{source}", "r") as file_in,
          open(f"{destination}", "w+") as file_out):
        file_out.write(file_in.read())

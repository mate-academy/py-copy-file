def copy_file(command: str) -> None:
    part_of_command = command.split(" ")
    if part_of_command[0] == "cp":
        if part_of_command[1] == part_of_command[2]:
            return
        with (
            open(part_of_command[1], "r") as file_in,
            open(part_of_command[2], "w") as file_out
        ):
            copy = file_in.read()
            file_out.write(copy)

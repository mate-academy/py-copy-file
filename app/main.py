def copy_file(command: str) -> None:
    new_command = command.split()
    if new_command[1] == new_command[2] or new_command[0] != "cp":
        print("Invalid input")
        return
    with (open(new_command[1], "r") as file_in,
          open(new_command[2], "w") as file_out):
        lines = file_in.readlines()
        file_out.writelines(lines)

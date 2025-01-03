def copy_file(command: str) -> None:
    r_command = command.split(" ")
    if len(r_command) != 3 or r_command[0] != "cp":
        print(f"Wrong command: {r_command[0]}")
        return

    if r_command[1] == r_command[2]:
        return

    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        for line in file_in.readlines():
            file_out.write(line)

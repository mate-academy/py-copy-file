def copy_file(command: str) -> None:
    splitted_command = command.split(" ")
    if splitted_command[1] == splitted_command[2]:
        return
    with (open(f"{splitted_command[1]}", "r") as file1,
          open(f"{splitted_command[2]}", "w") as file2):
        for line in file1.readlines():
            file2.write(line)

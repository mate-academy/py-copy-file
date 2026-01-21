def copy_file(command: str):
    splited_command = command.split(" ")
    if splited_command[0] != "cp" or splited_command[1] == splited_command[2]:
        return

    with open(splited_command[1], "r") as source, \
         open(splited_command[2], "a") as result:
        for line in source:
            result.write(line)

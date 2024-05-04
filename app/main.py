def copy_file(command: str) -> None:
    splitted_command = command.split(" ")
    if splitted_command[0] != "cp":
        print("Undefined command")
        return
    if splitted_command[1] == splitted_command[2]:
        return
    with open(splitted_command[1], "r") as file_in, \
         open(splitted_command[2], "w") as file_out:
        text = file_in.read()
        file_out.write(text)

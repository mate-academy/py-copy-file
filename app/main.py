def copy_file(command: str) -> None:
    if not "cp" in command:
        print("Does nothing")
        return
    if command.split()[1] == command.split()[2]:
        print("Does nothing")
        return
    file_1, file_2 = command.split()[1], command.split()[2]

    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        file_out.write(file_in.read())


copy_file("cp file.txt new_file.txt")

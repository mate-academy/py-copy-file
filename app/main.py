def copy_file(command: str) -> None:
    part_of_command = command.split()
    if len(part_of_command) != 3 or part_of_command[0] != "cp":
        print("Incorrect file format")
        return

    file_1, file_2 = part_of_command[1], part_of_command[2]

    if file_1 == file_2:
        print("Incorrect file name")
        return

    try:
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            file_out.write(file_in.read())
            print(f"File '{file_1}' successfully copy to '{file_2}'!")
    except FileNotFoundError:
        print(f"File {file_1} not found")

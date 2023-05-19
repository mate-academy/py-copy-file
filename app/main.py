def copy_file(command: str) -> None:
    parts_of_command = command.split()

    if parts_of_command[0] != "cp" or len(parts_of_command) != 3:
        print("You entered the wrong command!")
        return

    file_name = parts_of_command[1]
    new_file_name = parts_of_command[2]

    if file_name == new_file_name:
        print("You try to copy the file to a file with the same name!")
        return

    with (
        open(file_name, "r") as file_in,
        open(new_file_name, "w") as file_out
    ):
        file_out.write(file_in.read())
        print("The file was successfully copied.")

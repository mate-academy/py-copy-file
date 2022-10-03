def copy_file(command: str):
    try:
        input_command, file, new_file = command.split()
    except ValueError:
        print("Incorrect command")
        return

    if file == new_file:
        return

    if input_command == "cp":
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())

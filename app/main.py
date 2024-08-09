def copy_file(command: str) -> None:
    if not command:
        print("Command 'cp' is empty")

    copy_info = command.split()

    source_file = copy_info[1]
    target_file = copy_info[2]

    if len(copy_info) != 3:
        print("Command 'cp' is invalid")

    if source_file == target_file:
        print("The source and target files are identical. Does nothing.")
        return

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
        print("Copying completed!")

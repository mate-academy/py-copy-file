def copy_file(command: str) -> None:
    if command.startswith("cm"):
        command = command.replace("cm ", "")
    else:
        print("Unknown command")
    list_of_files_name = command.split(" ")
    if list_of_files_name[0] != list_of_files_name[1]:
        with (
            open(list_of_files_name[0], "r")
            as first_file,
            open(list_of_files_name[1], "w")
            as second_file
        ):
            second_file.write(first_file.read())

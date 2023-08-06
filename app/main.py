def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        print("Wrong command.")
        return
    file_original = split_command[1]
    file_duplicate = split_command[2]
    if file_original == file_duplicate:
        print("Can't copy file to file with the same name.")
        return
    with (open(file_original, "r") as original,
          open(file_duplicate, "w") as duplicate):
        duplicate.write(original.read())
        print("Copy was created.")

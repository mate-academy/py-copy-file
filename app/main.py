def copy_file(comnand: str) -> None:
    splited_command = comnand.split()
    if len(splited_command) != 3:
        print("Wrong command.")
        return
    file_original = splited_command[1]
    file_duplicate = splited_command[2]
    if file_original == file_duplicate:
        print("Can't copy file to file with the same name.")
        return
    with (open(file_original, "r") as original,
          open(file_duplicate, "w") as duplicate):
        duplicate.write(original.read())
        print("Copy was created.")

def copy_file(command: str):
    main_command, old_file, new_file = command.split()
    if main_command != "cp" or old_file == new_file:
        exit()
    with open(old_file, "r") as file_read:
        with open(new_file, "w") as file_write:
            file_write.writelines(file_read.readlines())


if __name__ == "__main__":
    copy_file(input("Enter command: "))

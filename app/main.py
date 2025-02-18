def copy_file(command: str) -> None:

    name_file = input("Enter file name: ")
    new_name_file = input("Enter a new file name: ")

    if name_file != new_name_file and command == "cp":
        with open(f"{name_file}.txt", "w") as file_in, \
                open(f"{new_name_file}.txt", "w") as file_out:
            file_in.write(f"{command} {name_file}.txt {new_name_file}.txt")
            file_out.write(f"{command} {name_file}.txt {new_name_file}.txt")

def copy_file(command: str) -> globals():
    parts_of_command = command.split()
    if len(parts_of_command) == 3 and parts_of_command[0] == "cp":
        source, copy = parts_of_command[1], parts_of_command[2]
    if source == copy:
        print("Does nothing")
    if source != copy:
        try:
            with open(source, "r") as file_in, open(copy, "w") as file_out:
                file_out.write(file_in.read())
        except FileNotFoundError:
            print("You did not make a file.txt")


if __name__ == "__main__":
    copy_file("cp example.txt new_example2.txt")

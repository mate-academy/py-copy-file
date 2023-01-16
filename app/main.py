def copy_file(command: str) -> None:
    file_in = command.split(" ")[1]
    file_out = command.split(" ")[2]
    with open(file_in, "r") as file_to_copy, \
            open(file_out, "a+") as copy_of_file:
        lines = file_to_copy.readlines()
        for line in lines:
            print(line.strip())
            copy_of_file.write(line)

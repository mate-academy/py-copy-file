def copy_file(string: str) -> None:
    command, from_file, to_file = string.split(" ")

    if from_file != to_file and command == "cp":
        with open(from_file, "r") as file_in, open(to_file, "w") as file_out:
            file_out.write(file_in.read())

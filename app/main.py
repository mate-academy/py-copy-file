def copy_file(command: str) -> None:
    words = command.split()

    if len(words) == 3 and words[0] == "cp":
        file_name = words[1]
        copy_name = words[2]

        if file_name == copy_name:
            return

        with open(file_name, "r") as file_in, open(copy_name, "w") as file_out:
            file_out.write(file_in.read())

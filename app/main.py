def copy_file(command: str) -> None:
    split_result = command.split()
    if len(split_result) == 3:
        cp, file, new_file = split_result
        if cp == "cp" and file != new_file:
            with open(file, "r") as file_in, open(new_file, "w") as file_out:
                file_out.write(file_in.read())

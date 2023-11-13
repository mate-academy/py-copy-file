def copy_file(command: str) -> None:
    files = command.split(" ")[1:]
    curr_file = files[0]
    new_file = files[1]

    if curr_file != new_file:
        with open(curr_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())

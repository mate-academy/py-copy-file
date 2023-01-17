def copy_file(command: str) -> None:
    cp, current_file, copied_file = command.split()
    with open(f"{current_file}.txt", "r") as file_in, \
            open(f"{copied_file}.txt", "w") as file_out:
        file_out.write(file_in.read())

def copy_file(command: str) -> None:
    file_names = command.split()

    first, second = file_names[1], file_names[2]

    if first == second:
        with open(first, "r") as file_in, open(second, "w") as file_out:
            file_out.write(file_in.read())

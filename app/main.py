def copy_file(command: str) -> None:
    all_data = command.split()

    if all_data[0] != "cp" or all_data[1] == all_data[2] or len(all_data) != 3:
        return

    file_to_copy = all_data[1]
    new_file = all_data[2]

    with open(file_to_copy, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())

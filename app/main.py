def copy_file(command: str) -> None:

    commands_data = command.split()
    first_file = commands_data[1]
    second_file = commands_data[2]

    if first_file == second_file:
        return

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        content_of_first_file = []
        for line in file_in:
            content_of_first_file.append(line)

        file_out.writelines(content_of_first_file)

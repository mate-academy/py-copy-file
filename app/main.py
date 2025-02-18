def copy_file(command: str) -> None:
    user_input = command.split()

    if (len(user_input) != 3
            or user_input[0] != "cp"
            or user_input[1] == user_input[2]):
        raise Exception("Please enter correct data.")

    _, file_to_copy, new_file = user_input

    with open(file_to_copy, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())

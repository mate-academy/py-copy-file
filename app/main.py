def copy_file(command: str):

    original_file = command.split(" ")[1]
    copied_file = command.split(" ")[2]

    if original_file == copied_file:
        return None

    # we can check if file with same name already exists
    try:
        with open(copied_file, "r"):
            pass
        return None
    except FileNotFoundError:
        pass

    with open(original_file, "r") as file_in, open(copied_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)

        return copied_file

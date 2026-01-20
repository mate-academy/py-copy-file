def copy_file(command: str) -> None:
    splited = command.split(" ")
    if len(splited) != 3 or splited[0] != "cp":
        return None

    original_file = splited[1]
    copied_file = splited[2]

    if original_file == copied_file:
        return None

    with (
        open(original_file, "r") as file_in,
        open(copied_file, "w") as file_out
    ):
        file_out.write(file_in.read())

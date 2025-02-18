def copy_file(command: str) -> None:
    if not validate(command):
        return
    com, file_name, new_file_name = command.split(" ")

    with (
        open(file_name, "r") as file_in,
        open(new_file_name, "w") as file_out
    ):
        file_out.write(file_in.read())


def validate(command: str) -> tuple | None:
    try:
        com, file_name, new_file_name = command.split(" ")
        if com != "cp":
            raise ValueError
        if file_name == new_file_name:
            return
    except ValueError:
        print("ERROR! Please enter command in the format:"
              "'cp file_name.txt new_file_name.txt'")
    else:
        return com, file_name, new_file_name


# copy_file("cp file.txt new_file.txt")

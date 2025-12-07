def copy_file(cp_command: str) -> None:
    file_names = cp_command.split()
    try:
        if file_names[1] == file_names[2]:
            return
    except IndexError:
        print("You must provide two arguments.")
        return
    if file_names[0] != "cp":
        return
    try:
        with (open(file_names[1], "r")
              as file_in, open(file_names[2], "w") as file_out):
            file_out.write(file_in.read())
    except OSError:
        print("Name Error. Try again.")


if __name__ == "__main__":
    try:
        copy_file()
    except TypeError:
        print("You must provide two arguments.")

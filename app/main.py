def copy_file(command: str) -> None:
    names_of_files = command.split()
    if len(names_of_files) < 3 or names_of_files[0] != "cp":
        return
    if names_of_files[1] == names_of_files[2]:
        return
    origin = names_of_files[1]
    new_copy = names_of_files[2]
    try:
        with open(origin, "r") as info_in, open(new_copy, "w") as info_out:
            content = info_in.read()
            info_out.write(content)
    except FileNotFoundError:
        return

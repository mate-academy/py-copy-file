def copy_file(command: str) -> None:
    file_names = command.split()

    if file_names[0] != "cp":
        raise ValueError(f"{file_names[0]} is not a copying command!")
    if len(file_names) != 3:
        raise ValueError(f"Expected two values for cp, got {len(file_names)}")
    if file_names[1] != file_names[2]:
        return None

    with (open(file_names[1], "r") as file_old,
            open(file_names[2], "w") as file_new):
        file_new.write(file_old.read())


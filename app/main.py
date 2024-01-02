def copy_file(command: str) -> None:
    key_elements = command.split()

    if key_elements[0] != "cp":
        raise ValueError("Invalid command. Maybe you meant 'cp...'?")
    if key_elements[1] == key_elements[2]:
        raise ValueError("Can't create a new file with the same name.")

    with (open(f"{key_elements[1]}", "r") as original_file,
          open(f"{key_elements[2]}", "w") as copied_file):
        copied_file.write(original_file.read())

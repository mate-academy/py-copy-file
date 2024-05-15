def copy_file(command: str) -> None:
    action, file_to_copy, new_file = command.split()
    if file_to_copy == new_file:
        pass
    else:
        with open(file_to_copy, "r") as f1, open(new_file, "w") as f2:
            f2.write("".join(f1.readlines()))

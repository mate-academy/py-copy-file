def copy_file(command: str) -> None:
    _, file, new_file = command.split()

    if file != new_file:
        with open(file, "r") as f_in, open(new_file, "w") as f_out:
            f_out.write(f_in.read())

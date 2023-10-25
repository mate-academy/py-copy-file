def copy_file(command: str) -> None:
    cp, old_file, new_file = command.split()
    if cp != "cp" or old_file == new_file:
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        old_file_text = file_in.read()
        file_out.write(old_file_text)

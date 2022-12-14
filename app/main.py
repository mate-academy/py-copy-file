def copy_file(comand: str) -> None:
    comand, old_file, new_file = comand.split()
    if old_file != new_file:
        with open(old_file, "r") as file_in, open(
                new_file, "w"
        ) as file_out:
            file_in_text = file_in.read()
            file_out.write(file_in_text)

def copy_file(command: str) -> None:
    parts = command.split()
    orig_file = parts[1]
    des_file = parts[2]
    if orig_file == des_file:
        return
    with open(orig_file, "r") as file_in, open(des_file, "w") as file_out:
        file_out.write(file_in.read())

def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    copy_file_command, sour_file, des_file = command.split()

    if sour_file == des_file or copy_file_command != "cp":
        return

    with open(sour_file, "r") as file_in, open(des_file, "w") as file_out:
        file_out.write(file_in.read())

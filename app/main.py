def copy_file(command: str) -> None:
    command_parts = command.split()
    copy_file_command = command_parts[0]
    sour_file = command_parts[1]
    des_file = command_parts[2]

    if sour_file == des_file:
        return
    else:
        print(f"{copy_file_command} {sour_file} {des_file}")
        with open(sour_file, "r") as file_in, open(des_file, "w") as file_out:
            file_out.write(file_in.read())

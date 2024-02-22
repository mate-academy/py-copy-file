def copy_file(command: str) -> None:
    sort_command = command.split()
    with open(sort_command[1], "r") as file_in, open(sort_command[2], "w") as file_out:
        file_out.write(f"{file_in}")

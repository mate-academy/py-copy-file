def copy_file(command: str) -> None:
    cp_command = command.split()
    if cp_command[0] == "cp" and cp_command[1] != cp_command[2]:
        with open(f"{cp_command[1]}", "r") as file_in, \
                open(f"{cp_command[2]}", "w") as file_out:
            information = file_in.read()
            file_out.write(information)

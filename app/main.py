def copy_file(command: str) -> None:
    cp, current_file, copied_file = command.split()
    if cp == "cp" and copied_file != current_file:
        with open(f"{current_file}", "r") as file_in, \
             open(f"{copied_file}", "w") as file_out:
            file_out.write(file_in.read())

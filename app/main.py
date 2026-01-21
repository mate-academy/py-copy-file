def copy_file(command: str) -> str | None:
    cp_command, file_for_copy, new_file = command.split()

    if cp_command != "cp":
        return "Invalid command format"

    if file_for_copy != new_file:
        with open(file_for_copy, "r") as f_in, open(new_file, "w") as f_out:
            f_out.write(f_in.read())
            print(f"File {file_for_copy} copied to {new_file}.")

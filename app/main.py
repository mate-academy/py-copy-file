def copy_file(command: str) -> None:
    cmd, file1_name, file2_name = command.split()

    if file1_name != file2_name and cmd == "cp":
        with open(f"{file1_name}", "r") as file_in, \
                open(f"{file2_name}", "a") as file_out:
            file_out.writelines(file_in.readlines())

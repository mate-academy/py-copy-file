def copy_file(command: str) -> None:
    cmd, file1_name, file2_name = command.split()

    if file1_name != file2_name and cmd == "cp":
        with (
            open(file1_name, "r") as file_in, open(file2_name, "w") as file_out
        ):
            file_out.writelines(file_in.readlines())

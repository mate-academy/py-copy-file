def copy_file(command: str) -> None:
    file1_name = command.split()[1]
    file2_name = command.split()[2]
    if file1_name != file2_name:
        with open(f"{file1_name}", "r") as file_in, \
                open(f"{file2_name}", "a") as file_out:
            for line in file_in:
                file_out.write(line)

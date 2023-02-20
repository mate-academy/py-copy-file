def copy_file(command: str) -> None:
    try:
        cp_command, file_in_name, file_out_name = command.split()
        if cp_command != "cp" or file_in_name == file_out_name:
            raise ValueError
        with (
            open(file_in_name, "r") as file_in,
            open(file_out_name, "w") as file_out
        ):
            file_out.write(file_in.read())
    except ValueError:
        print(
            "Your command must consist of: keyword 'cp',"
            " file name to copy and new file name, "
            "separated by spaces"
        )

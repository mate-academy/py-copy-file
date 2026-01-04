def copy_file(files_to_copy_path: str) -> None:
    files = files_to_copy_path.split()
    command = files[0]
    if command == "cp":
        if files[1] == files[2]:
            raise ValueError("Provide another file name.")
        try:
            with (open(files[1], "r") as file_in,
                  open(files[2], "w") as file_out):
                for line in file_in:
                    file_out.write(line)
        except (FileNotFoundError, PermissionError):
            raise ValueError("File not found or permission denied.")
    else:
        raise ValueError("Invalid command. Use: cp source_file target_file")

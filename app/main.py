def copy_file(command: str) -> None:
    check_command = command.split()
    if len(check_command) == 3:
        use_command = check_command[0]
        file_use = check_command[1]
        file_to_copy = check_command[2]
        if file_use == file_to_copy:
            return
        if use_command == "cp":
            try:
                with (open(file_use) as file_in,
                      open(file_to_copy, "w") as file_out):
                    for line in file_in.readlines():
                        file_out.write(line)

            except Exception:
                print(f"Source file '{file_use}' not found.")
    pass

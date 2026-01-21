def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3 and split_command[0] == "cp":
        if split_command[1] != split_command[2]:
            or_file, cp_file = split_command[1], split_command[2]
            try:
                with (open(or_file, "r")
                      as file_in, open(cp_file, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print(f"Error: Source file '{or_file}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")

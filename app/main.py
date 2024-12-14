def copy_file(command: str) -> None:
    command_line = command.split()
    command_name, source_file, copy_file_name = command_line
    is_valid_file_names = source_file != copy_file_name
    is_valid_command = command_name == "cp"
    is_valid_count_of_parameters = len(command_line) == 3
    if all([is_valid_command,
            is_valid_file_names,
            is_valid_count_of_parameters]):
        try:
            with (open(source_file, "r") as f_in,
                  open(copy_file_name, "w") as f_out
                  ):
                f_out.write(f_in.read())
        except FileNotFoundError:
            print(f"Source file {source_file} does not exist.")
        except Exception as e:
            print(f"Error occurred: {e}")

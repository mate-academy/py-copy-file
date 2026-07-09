def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        cp, source_file, target_file = command_parts
        if source_file != target_file and cp == "cp":
            try:
                with open(source_file, "r") as file_out, open(
                    target_file, "w"
                ) as file_in:
                    file_in.write(file_out.read())
            except FileNotFoundError:
                print(f"File '{source_file}' not found")

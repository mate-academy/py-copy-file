def copy_file(command: str) -> None:
    try:
        parts = command.split()
        if len(parts) == 3 and parts[0] == "cp":
            _, source_file, new_file = parts
            if source_file != new_file:
                with (
                    open(source_file, "r") as file_in,
                    open(new_file, "w") as file_out,
                ):
                    file_out.writelines(file_in)
    except FileNotFoundError:
        pass

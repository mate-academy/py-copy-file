def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        source_file_name = parts[1]
        target_file_name = parts[2]
        if source_file_name != target_file_name:
            try:
                with (
                    open(source_file_name, "r") as source_file_object,
                    open(target_file_name, "w") as target_file_object,
                ):
                    target_file_object.write(source_file_object.read())
            except FileNotFoundError:
                pass

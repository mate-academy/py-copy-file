def copy_file(command: str) -> None:
    action, source_file_name, target_file_name = command.split(maxsplit=2)

    if action != "cp":
        print("Invalid command format. Use: cp source_file target_file")
        return

    if source_file_name == target_file_name:
        print("Source and target file names are the same. "
              "Copy operation is not allowed.")
        return

    try:
        with (open(source_file_name, "r") as source,
              open(target_file_name, "w") as target):
            target.write(source.read())
        print(f"File '{source_file_name}' has "
              f"been copied to '{target_file_name}'.")
    except FileNotFoundError:
        print(f"Source file '{source_file_name}' not found.")

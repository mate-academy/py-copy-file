def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format.")
        return
    source_file, target_file = parts[1], parts[2]
    if source_file == target_file:
        print("Source and target files are the same. No need to copy.")
        return

    try:
        with (open(source_file, "r") as file_in,
              open(target_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File {source_file} not found.")
    except PermissionError:
        print(f"Permission denied while accessing "
              f"{source_file} or {target_file}.")
    except IsADirectoryError:
        print(f"Cannot open a directory instead of a file: "
              f"{source_file} or {target_file}.")
    except OSError as os_error:
        print(f"OS error occurred: {os_error}")
    except Exception as error:
        print(f"An error occurred: {error}")

def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Error: Invalid command format. "
              "Usage: cp <source> <destination>")
        return

    src, dst = parts[1], parts[2]

    if src == dst:
        print("Warning: Source and destination "
              "file names are the same. No action taken.")
        return

    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
        print(f"Success: File copied from '{src}' to '{dst}'")
    except FileNotFoundError:
        print(f"Error: Source file '{src}' not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{src}' or '{dst}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred — {e}")

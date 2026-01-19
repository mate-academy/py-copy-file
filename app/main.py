import os

def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, destination_file = parts[1], parts[2]

    # Check if source and destination are the same
    if source_file == destination_file:
        print(f"Error: The source file '{source_file}' and destination file are the same.")
        return

    if not os.path.exists(source_file):
        print(f"Error: {source_file} does not exist.")
        return

    if os.path.exists(destination_file):
        print(f"Error: {destination_file} already exists.")
        return

    try:
        with open(source_file, "r", encoding="utf-8") as source, open(destination_file, "w", encoding="utf-8") as destination:
            for line in source:
                destination.write(line)

        print(f"Successfully copied {source_file} to {destination_file}.")

    except FileNotFoundError:
        print(f"Error: One of the files was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing files.")
    except Exception as e:
        print(f"Error while copying file: {e}")


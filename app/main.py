import os

def copy_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        return

    if not os.path.exists(source_file):
        print(f"Error: {source_file} does not exist.")
        return

    if os.path.exists(destination_file):
        print(f"Error: {destination_file} already exists.")
        return

    try:
        with open(source_file, "r") as source, open(destination_file, "w") as destination:
            for line in source:
                destination.write(line)

        print(f"Successfully copied {source_file} to {destination_file}.")

    except IOError as e:
        print(f"Error while opening files: {e}")

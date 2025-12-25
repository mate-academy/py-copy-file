import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Error: The command format is incorrect")
        return
    _, source, destination = parts
    if source == destination:
        print("Error: Source and destination files cannot be the same.")
        return
    if not os.path.exists(source):
        print(f"Source file '{source}' does not exist.")
        return
    with (open(source, "r") as source_file,
          open(destination, "w") as destination_file):
        content = source_file.read()
        destination_file.write(content)

    print(f"File '{source}' has been copied to '{destination}'.")

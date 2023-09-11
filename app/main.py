import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Invalid command. "
              "Usage: cp source_file destination_file")
        return

    _, source_file, destination_file = parts

    if source_file == destination_file:
        print("Source and destination files "
              "have the same name. Doing nothing.")
        return

    if not os.path.exists(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    with open(source_file, "rb") as file_in, open(
            destination_file, "wb") as file_out:
        file_out.write(file_in.read())

    print(f"File {source_file}' copied to "
          f"'{destination_file}' successfully.")

import os


def copy_file(my_file: str) -> None:
    parts = my_file.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Please provide a valid 'cp' command.")
        return

    source_file, destination_file = parts[1], parts[2]
    if source_file == destination_file:
        print("Source and destination files"
              " have the same name. Nothing to copy.")
        return

    if not os.path.isfile(source_file):
        print(f"Source file '{source_file}' not found.")
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):

        data = file_in.read()
        file_out.write(data)
    print(f"Content from '{source_file}'"
          f" copied to '{destination_file}' successfully.")

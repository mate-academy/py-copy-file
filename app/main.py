import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format")

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        print("Change the name of file.")
        return

    with (open(source_file, "rb") as file_in,
          open(destination_file, "wb") as file_out):
        shutil.copyfileobj(file_in, file_out)

    print(f"File '{source_file}' successfully copied to '{destination_file}'.")

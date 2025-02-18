import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError(
            "Invalid command. Usage: "
            "cp source_file destination_file"
        )

    _, source_file, destination_file = parts

    if parts[0] == "cp" and source_file == destination_file:
        raise ValueError(
            "Source and destination files "
            "have the same name. Doing nothing."
        )

    if not os.path.exists(source_file):
        raise ValueError(f"Source file '{source_file}' does not exist.")

    with open(source_file, "rb") as file_in, open(
            destination_file, "wb") as file_out:
        file_out.write(file_in.read())

    print(f"File {source_file}' copied to "
          f"'{destination_file}' successfully.")

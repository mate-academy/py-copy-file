def copy_file(command: str) -> None:
    file_to_copy_path, destination_file_to_copy_path = command.split(" ")[1:]

    with (open(file_to_copy_path, "r") as file_in,
          open(destination_file_to_copy_path, "w") as file_out):
        file_out.write(file_in.read())

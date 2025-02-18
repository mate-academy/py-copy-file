from typing import Optional


def copy_file(command: str) -> Optional[None]:
    # Split the command into parts
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use: cp file.txt new_file.txt")
        return

    source_file, destination_file = parts[1], parts[2]

    # If the file names are the same, do nothing
    if source_file == destination_file:
        return

    # Copy the file content
    with (open(source_file, "r") as file_in,
          open(destination_file, "w")
          as file_out):
        content = file_in.read()
        file_out.write(content)


if __name__ == "__main__":
    copy_file("cp source_file.txt destination_file.txt")

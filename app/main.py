def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file, destination_file = parts[1], parts[2]

    if source_file == destination_file:
        return

    with (open(source_file, "r") as file_in,
          open(destination_file, "w") as file_out):
        file_out.write(file_in.read())


copy_file("cp file.txt file.txt")  # Does nothing

copy_file("cp file.txt new_file.txt")
open("file.txt").read() == open("new_file.txt").read()  # True

def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[1] != parts[2]:
        source_file = parts[1]
        destination_file = parts[2]

        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())


copy_file("cp file.txt file.txt")

copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())

def copy_file(command: str) -> None:
    with open("file.txt", "w") as f:
        f.write("Hello world!")

        parts = command.split()

        if len(parts) == 3 and parts[0] == "cp":
            source_file, destination_file = parts[1], parts[2]

            if source_file != destination_file:
                try:
                    with open(source_file, "r") as file_in, \
                            open(destination_file, "w") as file_out:
                        file_out.write(file_in.read())
                    print(f'File "{source_file}" '
                          f'copied to "{destination_file}"')
                except FileNotFoundError:
                    print(f"Source file {source_file} does not exist")

                else:
                    print(
                        "Source and destination file names are the same. "
                        "Doing nothing."
                    )
            else:
                print(
                    "Invalid command format. "
                    "Use 'cp source_file destination_file.'"
                )


copy_file("cp file.txt file.txt")

copy_file("cp file.txt new_file.txt")
print(open("file.txt").read() == open("new_file.txt").read())

def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print(
            "Invalid command format. Use: cp <source_file> <destination_file>"
        )
        return
    source_file, destination_file = parts[1], parts[2]
    if source_file == destination_file:
        print(
            "Source and destination files are the same. No action taken."
        )
        return
    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())
        print(f"File copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"Source file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


with open("file.txt", "w") as f:
    f.write("Hello, world!")

copy_file("cp file.txt new_file.txt")

print(open("file.txt").read())
print(open("new_file.txt").read())

copy_file("cp file.txt file.txt")
copy_file("cp missing.txt another.txt")

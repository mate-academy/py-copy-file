def copy_file(command: str) -> None:
    parts = command.split(" ")
    print(parts)
    source_path = parts[1]
    destination_path = parts[2]

    if source_path == destination_path:
        return

    with open(source_path, "r") as file_in, open(destination_path, "w") as file_out:
        for line in file_in:
            file_out.write(line)


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")

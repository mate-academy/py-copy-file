def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) < 3 or parts[0] != "cp":
        return

    source_path = parts[1]
    destination_path = parts[2]

    if source_path == destination_path:
        return

    with open(
            source_path, "r"
    ) as file_in, open(
            destination_path, "w"
    ) as file_out:
        file_out.writelines(file_in.readlines())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")

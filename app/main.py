def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[1] != parts[2]:
        source_file = parts[1]
        destination_file = parts[2]
        print(1)
        with open(source_file, "r") as file_in,\
                open(destination_file, "w") as file_out:
            for line in file_in:
                file_out.write(line)
    return

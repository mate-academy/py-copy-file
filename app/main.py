def copy_file(command: str) -> None:
    cp_command, source, destination_file = command.split()
    if cp_command != "cp" or source == destination_file:
        print("Command is not 'cp' or source "
              "and destination files are the same.")
        return

    with open(source, "r") as file_in, open(destination_file, "w") as file_out:
        file_out.write(file_in.read())
    print(f"Copied contents from {source} to {destination_file}")


copy_file("cp file.txt new_file.txt")

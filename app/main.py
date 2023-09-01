def copy_file(command: str):

    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format!")
        return

    source, dest = parts[1], parts[2]

    if source == dest:
        return

    with open(source, 'r') as file_in, open(dest, 'w') as file_out:
        file_out.write(file_in.read())

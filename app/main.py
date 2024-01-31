def copy_file(command_line: str) -> None:
    parts = command_line.split()

    if len(parts) == 3 and parts[0] == "cp":
        source = parts[1]
        dest = parts[2]

        if source == dest:
            print("Do nothing")
            return

        try:
            with open(source, "r") as file_in, open(dest, "w") as file_out:
                file_out.write(file_in.read())
            print(f"File {source} coppied to destination")
        except FileNotFoundError:
            print(f"File {source} not exists")
    else:
        print("invalid command")

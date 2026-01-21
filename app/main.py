def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        src = parts[1]
        dst = parts[2]
        if src != dst:
            try:
                with open(src, "r") as file_in, open(dst, "w") as file_out:
                    line = file_in.read()
                    file_out.write(line)
            except FileNotFoundError as e:
                print(f"Error: {e}")

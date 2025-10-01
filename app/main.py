def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        return
    cmd, src, dst = parts
    if cmd != "cp":
        print("Unknown command. Did you mean 'cp'?")
        return
    if src == dst:
        return
    try:
        with (open(src, "r", encoding="utf-8") as file_in,
              open(dst, "w", encoding="utf-8") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("File not found")

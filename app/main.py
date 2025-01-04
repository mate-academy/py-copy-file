def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        print("Invalid command format")
        return

    cmd, src, dest = parts

    if src == dest:
        print("Source and destination file names are the same. "
              "Operation aborted.")
        return

    # Copy the file if names are different
    with open(src, "r") as file_in, open(dest, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

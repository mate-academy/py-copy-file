# write your code here
def copy_file(command: str) -> None:
    # command format: "cp source.txt dest.txt"
    parts = command.split()

    # Expect exactly 3 parts: ["cp", "source", "dest"]
    if len(parts) != 3:
        return

    _, src, dst = parts

    # Do nothing if names are the same
    if src == dst:
        return

    # Copy file contents
    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())

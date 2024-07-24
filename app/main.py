def copy_file(command: str) -> None:
    args = command.split()
    if len(args) < 3:
        raise FileNotFoundError("No file name specified.")

    file1, file2 = args[1:]

    if file1 == file2:
        raise ValueError("Source and destination filenames are the same.")

    if file1 != file2:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())


if __name__ == "__main__":
    import sys
    copy_file(" ".join(sys.argv[1:]))

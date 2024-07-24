def copy_file(command: str) -> None:
    args = command.split()
    if len(args) < 3:
        raise FileNotFoundError("No file name specified.")

    file1 = command.split()[1]
    file2 = command.split()[2]

    if not file1 == file2:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())


if __name__ == "__main__":
    import sys
    copy_file(" ".join(sys.argv[1:]))

def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        raise ValueError("Must be [cmd, file1, file2]")
    cmd, src_file, dst_file = command_parts

    if src_file == dst_file:
        return
    if cmd != "cp":
        raise ValueError("wrong command accept only cp - Copy")
    try:
        with (open(src_file, "r", encoding="utf-8") as file_in,
              open(dst_file, "w", encoding="utf-8") as file_out):
            file_out.write(file_in.read())
    except (ValueError, FileNotFoundError) as e_info:
        print(e_info)


def main() -> None:
    copy_file("cp file.txt new_file.txt")


if __name__ == "__main__":
    main()

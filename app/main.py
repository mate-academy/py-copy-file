def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3 or parts[0] != "cp":
        print("Command is wrong!")
        return

    src, dest = parts[1], parts[2]

    if src == dest:
        return

    with open(src, "r") as file_in, open(dest, "w") as file_out:
        file_out.writelines(file_in.readlines())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")

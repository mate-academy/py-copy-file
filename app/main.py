def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        return
    src, dst = parts[1], parts[2]

    if src == dst:
        return
    try:
        with open(src, "r") as src_file, open(dst, "w") as dst_file:
            dst_file.write(src_file.read())
    except FileNotFoundError:
        print("Error: file not found")
    except FileExistsError:
        print("Error: file already exists")
    except IOError as e:
        print("Error: cannot copy file", e)

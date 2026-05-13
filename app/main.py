def copy_file(command: str) -> None:

    parts_file = command.split()
    if len(parts_file) != 3:
        print("Incorrect count of arguments")
        return
    if parts_file[0] != "cp":
        print("Excepted: cp")
        return
    fst_file = parts_file[1]
    snd_file = parts_file[2]
    if fst_file == snd_file:
        print("Both files are the same")
        return

    try:
        with (
            open(fst_file, "r") as source_file,
            open(snd_file, "w") as destination_file
        ):
            destination_file.write(source_file.read())
    except FileNotFoundError:
        print("File {fst_file} not found")
        return

def copy_file(command: str) -> None:
    try:
        cmd, filename1, filename2 = command.split(" ")
        if not cmd == "cp":
            return
        if filename1 == filename2:
            return

        with open(filename1, "r") as file_in, open(filename2, "w") as file_out:
            file_out.write(file_in.read())
    except Exception as e:
        print(e)
        return

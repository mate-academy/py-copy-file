def copy_file(command: str) -> None:
    data = command.split(" ")

    if data[0] != "cp" or len(data) != 3:
        return

    if data[1] == data[2]:
        return
    try:
        with open(data[1], "r") as file, open(data[2], "w") as file_new:
            file_new.write(file.read())
    except FileNotFoundError:
        print(f"File {data[1]} not found.")

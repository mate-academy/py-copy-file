def copy_file(comand: str) -> None:
    words = comand.split(" ")
    if words[0] != "cp" or len(words) != 3:
        return
    origin = words[1]
    destination = words[2]
    if origin == destination:
        return
    try:
        with open(origin, "r") as file_in, open(destination, "w") as file_out:
            file_out.write(file_in.read())
    except Exception as e:
        print(e)

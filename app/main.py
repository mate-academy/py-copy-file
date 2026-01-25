from pathlib import Path


def copy_file(comand: str) -> None:
    words = comand.split(" ")
    if words[0] != "cp" or len(words) != 3:
        return
    origin = words[1]
    destination = words[2]
    if Path(destination).is_file():
        return
    text_file = ""
    try:
        with open(origin, "r") as file_in, open(destination, "w") as file_out:
            for line in file_in.readlines():
                text_file += line
            file_out.write(text_file)
    except Exception as e:
        print(e)

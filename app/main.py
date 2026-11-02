def copy_file(command: str) -> None:
    arr = command.split(" ")
    try:
        if arr[0] != "cp" or arr[1] == arr[2]:
            return
        with open(arr[1], "r") as f1, open(arr[2], "w") as f2:
            for i in f1.readlines():
                f2.write(i)
    except Exception:
        return

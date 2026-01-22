def copy_file(path: str) -> None:
    data = path.split(" ")
    if data[1] != data[2] and data[0] == "cp" and len(data) == 3:
        file_path_1 = f"app\\{data[1]}"
        file_path_2 = f"app\\{data[2]}"
        try:
            with open(file_path_1, "r") as f1, open(file_path_2, "w") as f2:
                f2.write(f1.read())
        except FileNotFoundError:
            print(f"File {data[1]} not found")
        else:
            print(f"File {data[1]} copied to {data[2]}")

def copy_file(request: str) -> None:
    splited_request = request.split()
    if (len(splited_request) == 3
            and splited_request[0] == "cp"
            and splited_request[1] != splited_request[2]):
        try:
            with (open(splited_request[1], "r") as current_file,
                  open(splited_request[2], "w") as new_file):
                new_file.write(current_file.read())
        except FileNotFoundError:
            print(f"File {splited_request[1]} not found.")

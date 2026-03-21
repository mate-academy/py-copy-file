

def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3:
        param, old_name, new_name = parts[0], parts[1], parts[2]

        if param == "cp" and old_name != new_name:
            try:
                with open(old_name, "rb") as src:
                    data = src.read()
                with open(new_name, "wb") as dst:
                    dst.write(data)
            except FileNotFoundError:
                print(f"Source file '{old_name}' not found."
                      f" Skipping copy.")

def copy_file(cp_command: str) -> None:
    while True:
        try:
            with open(f"{file_name}.txt", "w"):
                pass
            break
        except OSError:
            print("Name Error. Try again.")


    with open(f"{file_name}.txt", "w") as file:
        file.write(joined_text)


if __name__ == "__main__":
    copy_file()
import os.path


def copy_file(command: str) -> None:
    command = command.strip()
    words = command.split()

    if len(words) <= 1:
        print(
            "You've entered wrong command! "
            "Try something like this: 'cp file.txt file.txt'"
        )
        return

    first_file, second_file = words[1], words[2]

    if not os.path.exists(first_file):
        print("The file you want to copy doesn't exist, try another name!")
        return

    if first_file == second_file:
        return

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())

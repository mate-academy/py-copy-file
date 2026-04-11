import shutil


def copy_file(command: str) -> None:
    parts = command.split()  # або shlex.split(command) для пробілів у іменах
    if len(parts) != 3 or parts[0] != "cp":
        print("Помилка: використовуйте формат 'cp source destination'")
        return

    src, dst = parts[1], parts[2]

    if src == dst:
        return

    try:
        # Найкращий спосіб для копіювання будь-яких файлів (текст, фото тощо)
        shutil.copy2(src, dst)
    except FileNotFoundError:
        print(f"Файл {src} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

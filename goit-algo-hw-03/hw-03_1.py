from colorama import Fore, Style
from pathlib import Path
import os
import sys
import shutil

def parse_folder(src_path, dest_path):
    try:
        for el in src_path.iterdir():
            if el.is_dir():
                parse_folder(el, dest_path)
            else:
                file_extension = el.suffix[1:]  # Отримуємо розширення файлу без крапки
                if file_extension:  # Якщо у файлу є розширення
                    new_dir = dest_path / file_extension
                    new_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(el, new_dir / el.name)
                else:  # Якщо у файлу немає розширення
                    new_dir = dest_path / "no_extension"
                    new_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(el, new_dir / el.name)
    except Exception as e:
        print(f"{Fore.RED}Помилка при обробці {src_path}: {e}")
        print(Style.RESET_ALL)

def show_directory_structure(src_directory_path, dest_directory_path):
    src_path = Path(src_directory_path)
    dest_path = Path(dest_directory_path)
    if not src_path.exists() or not src_path.is_dir():
        print(f"{Fore.RED}Шлях {src_directory_path} не існує або не є директорією.")
        return print(Style.RESET_ALL)

    if not dest_path.exists():
        dest_path.mkdir(parents=True)

    parse_folder(src_path, dest_path)
    print(Style.RESET_ALL)

def show_usage():
    if os.name == "nt":
        print(f"{Fore.GREEN}Використання: python main.py C:\\шлях\\до\\вихідної\\директорії [C:\\шлях\\до\\директорії\\призначення]")
    else:
        print(f"{Fore.GREEN}Використання: python main.py /шлях/до/вихідної/директорії [/шлях/до/директорії/призначення]")
    return print(Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        show_usage()
    else:
        src_directory_path = sys.argv[1]
        dest_directory_path = sys.argv[2] if len(sys.argv) == 3 else 'dist'
        show_directory_structure(src_directory_path, dest_directory_path)

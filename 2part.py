import os
import shlex
import argparse

# Аргументы командной строки
parser = argparse.ArgumentParser()
parser.add_argument("--vfs_path", help="Путь к виртуальной файловой системе", default=None)
parser.add_argument("--script", help="Стартовый скрипт с командами", default=None)
args = parser.parse_args()

vfs_path = args.vfs_path
script_file = args.script

# Настройки эмулятора
username = os.environ.get("USERNAME") or os.environ.get("USER")
vfs_name = "MyVFS"

print("=== Конфигурация ===")
print(f"Путь к VFS: {vfs_path}")
print(f"Стартовый скрипт: {script_file}")
print("====================")

# Функция парсинга
def parse_command(command: str):
    return shlex.split(command)

# Функция выполнения команд
def execute_command(args):
    if not args:
        return False

    command = args[0]
    command_args = args[1:]

    if command == "exit":
        print("Выход из виртуальной файловой системы")
        return True

    elif command == "ls":
        print(f"[ls] Аргументы: {command_args}")

    elif command == "cd":
        print(f"[cd] Аргументы: {command_args}")

    else:
        print(f"Неизвестная команда: {command}")

    return False

if script_file:
    try:
        with open(script_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                print(f"{username}@{vfs_name}> {line}")  # имитация ввода
                args = parse_command(line)
                stop = execute_command(args)
                if stop:
                    break
    except FileNotFoundError:
        print(f"Скрипт не найден: {script_file}")
else:
    while True:
        user_input = input(f"{username}@{vfs_name}> ")
        if not user_input.strip():
            continue
        args = parse_command(user_input)
        stop = execute_command(args)
        if stop:
            break
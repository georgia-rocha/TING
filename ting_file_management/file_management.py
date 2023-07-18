import sys
import os


def txt_importer(path_file):
    file_name = os.path.basename(path_file)
    ext = os.path.splitext(file_name)

    if ext[1] != '.txt':
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            return file.read().split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

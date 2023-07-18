import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    new = create(path_file)

    if path_file not in instance.queue:
        instance.enqueue(path_file)
        return print(new, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)

    path_file = instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    if position < 0 or position > len(instance):
        return print("Posição inválida", file=sys.stderr)

    file_search = instance.search(position)
    new = create(file_search)

    print(new, file=sys.stdout)


def create(path_file):
    file = txt_importer(path_file)
    new = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    return new

import sys
from queue import Queue
from file_management import txt_importer


def process(path_file, instance: Queue):
    data_file = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data_file),
        "linhas_do_arquivo": data_file,
    }

    for index in instance.__len__():
        if path_file == instance.search(index)["nome_do_arquivo"]:
            pass
        else:
            instance.enqueue(new_dict)
            sys.stdout.write(new_dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None

    data_file = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data_file),
        "linhas_do_arquivo": data_file,
    }

    instance.enqueue(new_dict)
    sys.stdout.write(str(new_dict))
    # print(str(new_dict)) mais um push


def remove(instance: Queue):
    removed_file = instance.dequeue()

    if removed_file is None:
        print("Não há elementos")
    else:
        print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso"
        )


def file_metadata(instance: Queue, position):
    try:
        searched_file = instance.search(position)
        print(searched_file)
    except IndexError:
        sys.stderr.write("Posição inválida\n")

from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    word_lowed = word.lower()

    found_files = []

    for index_file in range(len(instance)):
        actual_file = instance.search(index_file)
        file_found = {
            "palavra": word,
            "arquivo": actual_file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for index_row in range(len(actual_file["linhas_do_arquivo"])):
            line_lowed = actual_file["linhas_do_arquivo"][index_row].lower()
            if word_lowed in line_lowed:
                file_found["ocorrencias"].append(
                    {
                        "linha": index_row + 1,
                    }
                )
        if file_found["ocorrencias"]:
            found_files.append(file_found)

    return found_files


def search_by_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""

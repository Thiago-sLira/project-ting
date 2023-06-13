from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    new_regular_customer = {
        "nome_do_arquivo": "Fulado de Tal",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["Um", "cliente", "regular"],
    }

    new_priority_customer = {
        "nome_do_arquivo": "Ciclano de Tal",
        "qtd_linhas": 6,
        "linhas_do_arquivo": ["Um", "cliente", "prioritário", "está", "presente"],
    }

    priority_queue = PriorityQueue()

    # priority_queue.enqueue()

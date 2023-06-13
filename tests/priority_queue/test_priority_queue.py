from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    new_regular_customer = {
        "nome_do_arquivo": "Fulado de Tal",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["Um", "cliente", "regular"],
    }

    new_priority_customer = {
        "nome_do_arquivo": "Ciclano de Tal",
        "qtd_linhas": 6,
        "linhas_do_arquivo": ["Um", "cliente", "prioritário", "está", "aqui"],
    }

    priority_queue = PriorityQueue()

    priority_queue.enqueue(new_regular_customer)
    assert len(priority_queue) == 1

    priority_queue.enqueue(new_priority_customer)
    assert len(priority_queue) == 2

    assert priority_queue.search(0)["qtd_linhas"] == 3
    assert priority_queue.search(1)["qtd_linhas"] == 6

    priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 1

    with pytest.raises(IndexError):
        priority_queue.search(500)

    # priority_queue.enqueue(new_regular_customer)

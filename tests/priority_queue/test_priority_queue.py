from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_path = [
    {
        "nome_do_arquivo": "file1.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ['linhas']
    },
    {
        "nome_do_arquivo": "file2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": ['linhas']
    },
    {
        "nome_do_arquivo": "file3.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": ['linhas']
    },
]


def test_basic_priority_queueing():
    instance = PriorityQueue()

    assert instance.is_priority(mock_path[0]) is True
    assert instance.is_priority(mock_path[1]) is False
    assert instance.is_priority(mock_path[2]) is False

    instance.enqueue(mock_path[0])
    instance.enqueue(mock_path[1])
    instance.enqueue(mock_path[2])

    assert len(instance.high_priority) == 1
    assert len(instance.regular_priority) == 2
    assert len(instance) == 3

    assert instance.search(0) == mock_path[0]

    instance.dequeue()
    assert len(instance.high_priority) == 0
    assert len(instance.regular_priority) == 2

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        instance.search(55)

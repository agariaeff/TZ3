from main import main
import time


def test_main_time_small():
    n = 100
    start_time = time.time()
    for i in range(0, n):
        main('test_inputs/input_1.txt')
    total_time = (time.time() - start_time) / n
    assert total_time < 1


def test_main_time_standard():
    n = 100
    start_time = time.time()
    for i in range(0, n):
        main('test_inputs/input_2.txt')
    total_time = (time.time() - start_time) / n
    assert total_time < 1


def test_main_time_large():
    start_time = time.time()
    main('test_inputs/input_3.txt')
    total_time = (time.time() - start_time)
    assert total_time < 1

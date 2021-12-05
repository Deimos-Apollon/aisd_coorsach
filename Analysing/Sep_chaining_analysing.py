import time
from collections import Counter

import matplotlib.pyplot as plt

from Hash_table_separate_chaining.Hash_table_sep_chain import HashTableSepChain
from random import randint


def analyse_insert_with_resize(ht, arr):
    times_number_for_table_size = Counter()
    all_times_for_table_size = Counter()

    best_times = Counter()
    worst_times = Counter()
    was_last_division = False
    for elem_pair in arr:
        was_last_division = False
        table_size = ht.__size__
        start = time.process_time()
        ht.insert(elem_pair[0], elem_pair[1])
        total_time = time.process_time() - start
        all_times_for_table_size[table_size] += total_time
        if total_time < best_times[table_size] or (not best_times[table_size]):
            best_times[table_size] = total_time
        if total_time > worst_times[table_size]:
            worst_times[table_size] = total_time
        if table_size == ht.__size__:
            times_number_for_table_size[table_size] += 1
        else:
            all_times_for_table_size[table_size] /= times_number_for_table_size[table_size]
            was_last_division = True

    if not was_last_division:
        all_times_for_table_size[ht.__size__] /= times_number_for_table_size[ht.__size__]

    plt.figure()
    plt.title("График зависимости лучшего времени для вставки элемента\n"
              " от размера таблицы c учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Лучшее время для операции вставки, сек")

    plt.plot(best_times.keys(), best_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/insertion/best_times_with_resize.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости среднего времени для вставки элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции вставки, сек")
    plt.plot(all_times_for_table_size.keys(), all_times_for_table_size.values(), '--o')
    plt.savefig("Sep_chaining_figures/insertion/mean_times_with_resize.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости худшего времени для вставки элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Худшее время для операции вставки, сек")
    plt.plot(worst_times.keys(), worst_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/insertion/worst_times_with_resize.png", bbox_inches="tight")


def analyse_insert_without_resize(ht, arr):
    times_number_for_table_size = Counter()
    all_times_for_table_size = Counter()

    best_times = Counter()
    worst_times = Counter()
    was_last_division = False
    for elem_pair in arr:
        was_last_division = False
        table_size = ht.__size__
        start = time.process_time()
        ht.insert(elem_pair[0], elem_pair[1])
        total_time = time.process_time() - start
        if table_size == ht.__size__:
            times_number_for_table_size[table_size] += 1
            all_times_for_table_size[table_size] += total_time
            if total_time < best_times[table_size] or (not best_times[table_size]):
                best_times[table_size] = total_time
            if total_time > worst_times[table_size]:
                worst_times[table_size] = total_time
        else:
            all_times_for_table_size[table_size] /= times_number_for_table_size[table_size]
            was_last_division = True

    if not was_last_division:
        all_times_for_table_size[ht.__size__] /= times_number_for_table_size[ht.__size__]

    plt.figure()
    plt.title("График зависимости лучшего времени для вставки элемента\n"
              " от размера таблицы без учёта resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Лучшее время для операции вставки, сек")

    plt.plot(best_times.keys(), best_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/insertion/best_times_without_resize.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости среднего времени для вставки элемента\n"
              " от размера таблицы без учёта resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции вставки, сек")
    plt.plot(all_times_for_table_size.keys(), all_times_for_table_size.values(), '--o')
    plt.savefig("Sep_chaining_figures/insertion/mean_times_without_resize.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости худшего времени для вставки элемента\n"
              " от размера таблицы без учёта resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("худшее время для операции вставки, сек")
    plt.plot(worst_times.keys(), worst_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/insertion/worst_times_without_resize.png", bbox_inches="tight")


# TODO сравнение нескольких таблиц
def analyse_find(ht, arr):
    times_number_for_table_size = Counter()
    all_times_for_table_size = Counter()
    best_times = Counter()
    worst_times = Counter()
    was_last_division = False

    for elem_pair in arr:
        was_last_division = False
        table_size = ht.__size__
        start = time.process_time()
        ht.find(elem_pair[0])
        total_time = time.process_time() - start
        all_times_for_table_size[table_size] += total_time
        if total_time < best_times[table_size] or (not best_times[table_size]):
            best_times[table_size] = total_time
        if total_time > worst_times[table_size]:
            worst_times[table_size] = total_time
        if table_size == ht.__size__:
            times_number_for_table_size[table_size] += 1
        else:
            all_times_for_table_size[table_size] /= times_number_for_table_size[table_size]
            was_last_division = True

    if not was_last_division:
        all_times_for_table_size[ht.__size__] /= times_number_for_table_size[ht.__size__]

    plt.figure()
    plt.title("График зависимости лучшего времени для поиска элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Лучшее время для операции поиска, сек")

    plt.plot(best_times.keys(), best_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/find/best_times.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости среднего времени для поиска элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции поиска, сек")
    plt.plot(all_times_for_table_size.keys(), all_times_for_table_size.values(), '--o')
    plt.savefig("Sep_chaining_figures/find/mean_times.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости худшего времени для поиска элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Худшее время для операции поиска, сек")
    plt.plot(worst_times.keys(), worst_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/find/worst_times.png", bbox_inches="tight")


def analyse_pop(ht, arr):
    times_number_for_table_size = Counter()
    all_times_for_table_size = Counter()
    best_times = Counter()
    worst_times = Counter()
    was_last_division = False

    for elem_pair in arr:
        was_last_division = False
        table_size = ht.__size__
        start = time.process_time()
        ht.find(elem_pair[0])
        total_time = time.process_time() - start
        all_times_for_table_size[table_size] += total_time
        if total_time < best_times[table_size] or (not best_times[table_size]):
            best_times[table_size] = total_time
        if total_time > worst_times[table_size]:
            worst_times[table_size] = total_time
        if table_size == ht.__size__:
            times_number_for_table_size[table_size] += 1
        else:
            all_times_for_table_size[table_size] /= times_number_for_table_size[table_size]
            was_last_division = True

    if not was_last_division:
        all_times_for_table_size[ht.__size__] /= times_number_for_table_size[ht.__size__]

    plt.figure()
    plt.title("График зависимости лучшего времени для вставки элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции вставки, сек")

    plt.plot(best_times.keys(), best_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/pop/best_times_with_resize.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости среднего времени для вставки элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции вставки, сек")
    plt.plot(all_times_for_table_size.keys(), all_times_for_table_size.values(), '--o')
    plt.savefig("Sep_chaining_figures/pop/mean_times_with_resize.png", bbox_inches="tight")

    plt.figure()
    plt.title("График зависимости худшего времени для вставки элемента\n"
              " от размера таблицы с учётом resize")
    plt.xlabel("Размер таблицы")
    plt.ylabel("Среднее время для операции вставки, сек")
    plt.plot(worst_times.keys(), worst_times.values(), '--o')
    plt.savefig("Sep_chaining_figures/pop/worst_times_with_resize.png", bbox_inches="tight")


if __name__ == "__main__":
    ht = HashTableSepChain()
    random_arr = [(randint(0, 100000), i) for i in range(100000)]

    # checking insertion
    analyse_insert_without_resize(ht, random_arr)

    # checking insertion with resize
    ht.clear()
    analyse_insert_with_resize(ht, random_arr)

import sys

# реализация MaxHeap (максимальная куча)
class MaxHeap:
    """
    реализация max-heap на массиве (1...).
    Поддерживает push(x), peek(), pop().
    Реализована очистка: мы будем хранить в куче кандидаты (значения сумм),
    а проверку актуальности (существует ли в total_to_cities) делаем снаружи.
    """
    def __init__(self):
        self.a = []  # внутренний список, 0-indexed; будем использовать 0..len-1
    def __len__(self):
        return len(self.a)
    def push(self, x):
        # вставка (x) в max-heap
        self.a.append(x)
        i = len(self.a) - 1
        # просеивание вверх
        while i > 0:
            p = (i - 1) // 2
            if self.a[p] < self.a[i]:
                self.a[p], self.a[i] = self.a[i], self.a[p]
                i = p
            else:
                break
    def peek(self):
        if not self.a:
            return None
        return self.a[0]
    def pop(self):
        if not self.a:
            return None
        top = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            # просеивание вниз
            i = 0
            n = len(self.a)
            while True:
                l = 2*i + 1
                r = 2*i + 2
                largest = i
                if l < n and self.a[l] > self.a[largest]:
                    largest = l
                if r < n and self.a[r] > self.a[largest]:
                    largest = r
                if largest == i:
                    break
                self.a[i], self.a[largest] = self.a[largest], self.a[i]
                i = largest
        return top


def main():
    data = sys.stdin.read().strip().split()
    # будем парсить вход по токенам (просто и надежно)
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return

    # Храним данные о миллиардерах
    # name -> wealth (int)
    wealth = {}
    # name -> current city (str)
    person_city = {}

    # city_total: city -> суммарное состояние (int)
    city_total = {}

    for _ in range(n):
        # каждая строка: имя, город, состояние
        name = next(it)
        city = next(it)
        w = int(next(it))
        wealth[name] = w
        person_city[name] = city
        city_total.setdefault(city, 0)
        city_total[city] += w

    # Далее: m, k
    m = int(next(it))
    k = int(next(it))

    # events_by_day[d] = список перемещений, которые вступают в силу в день d (т.е. moves with orig_day = d-1)
    # индексация 1..m
    events_by_day = [[] for _ in range(m + 2)]  # +2 чтобы безопасно обращаться к m+1
    # Список всех городов, которые могут появиться (чтобы в конце вывести все с ненулём)
    # Но фактически города будут добавляться в city_total по мере появления.

    for _ in range(k):
        day_num = int(next(it))         # номер дня (1..m-1), отбывают поздно вечером
        person = next(it)
        dest = next(it)
        eff_day = day_num + 1  # прибытие утром следующего дня: изменение вступает в силу с eff_day
        if eff_day <= m:
            events_by_day[eff_day].append((person, dest))
        # если eff_day > m — перемещение происходит после рассматриваемого периода, можно игнорировать

    # --- Подготовка вспомогательных структур для быстрого поддержания максимаума ---
    # total_to_cities: total -> set(city)
    total_to_cities = {}
    def add_city_to_total(city, total):
        s = total_to_cities.get(total)
        if s is None:
            s = set()
            total_to_cities[total] = s
        s.add(city)

    def remove_city_from_total(city, total):
        s = total_to_cities.get(total)
        if s is None:
            return
        if city in s:
            s.remove(city)
            if not s:
                # оставляем ключ, но со множеством пустым
                # для удобства можно удалить ключ
                del total_to_cities[total]

    # Инициализируем total_to_cities по city_total
    for c, tot in city_total.items():
        add_city_to_total(c, tot)

    # Также потенциально есть города с 0 суммой (например, цель перемещения), но мы добавим их при первом обновлении.

    # Создадим MaxHeap и заполним начальными суммами
    heap = MaxHeap()
    # Чтобы ускорить, добавляем в кучу все существующие totals
    for tot in total_to_cities.keys():
        heap.push(tot)

    # Счётчик дней, когда город был лидером
    city_days = {}  # city -> количество дней

    # Вспомогательная функция: получить текущую максимальную сумму, очищая кучу от устаревших значений
    def get_current_max_total():
        while True:
            top = heap.peek()
            if top is None:
                return None
            # если в total_to_cities есть непустое множество для top — он актуален
            s = total_to_cities.get(top)
            if s is not None and len(s) > 0:
                return top
            # иначе — устаревшее значение, выкинем его и продолжим
            heap.pop()

    # Список дней, когда происходят изменения (эффективные дни), отсортируем
    event_days = [d for d in range(1, m+1) if events_by_day[d]]
    event_days.sort()

    # Обрабатываем интервалы:
    cur_day = 1
    idx = 0
    # Обработать интервалы между событиями и после последнего события до m
    # Для удобства добавим фиктивную границу next_change = m+1
    event_days_with_end = event_days + [m + 1]

    for next_change in event_days_with_end:
        # промежуток [cur_day .. next_change - 1] — в нём состояние не меняется
        if cur_day <= next_change - 1:
            interval_len = (next_change - cur_day)
            # узнаём текущее максимальное значение
            cur_max = get_current_max_total()
            if cur_max is not None:
                winners = total_to_cities.get(cur_max, set())
                if winners:
                    # добавляем всем победителям interval_len дней
                    for city in winners:
                        city_days[city] = city_days.get(city, 0) + interval_len
            # сдвигаем текущую дату
        # теперь переходим на день next_change — нужно применить все события, вступающие в силу в этот день,
        # и затем продолжить (следующий интервал начнётся с этой даты).
        if next_change <= m:
            # применяем все события дня next_change (все перемещения, прибывающие в этот день утром)
            for (person, dest) in events_by_day[next_change]:
                w = wealth[person]
                old_city = person_city[person]
                new_city = dest
                if old_city == new_city:
                    # если переезд в тот же город — ничего не меняется
                    person_city[person] = new_city
                    continue

                # Уменьшаем старую сумму
                old_total = city_total.get(old_city, 0)
                new_old_total = old_total - w
                # обновляем структуры: remove old_city от old_total, добавить к new_old_total
                remove_city_from_total(old_city, old_total)
                # обновление city_total
                if new_old_total == 0:
                    # если стала 0 — сохраняем 0 как валидную сумму (город существует, просто 0)
                    city_total[old_city] = 0
                    add_city_to_total(old_city, 0)
                    heap.push(0)
                else:
                    city_total[old_city] = new_old_total
                    add_city_to_total(old_city, new_old_total)
                    heap.push(new_old_total)

                # Увеличиваем сумму нового города
                old_total_new_city = city_total.get(new_city, 0)
                new_total_new_city = old_total_new_city + w
                # если ранее new_city не было в словаре, старое значение 0
                # удаляем город из множества old_total_new_city (если он там был)
                if old_total_new_city in total_to_cities and new_city in total_to_cities[old_total_new_city]:
                    remove_city_from_total(new_city, old_total_new_city)
                # записываем новую сумму
                city_total[new_city] = new_total_new_city
                add_city_to_total(new_city, new_total_new_city)
                heap.push(new_total_new_city)

                # обновляем информацию о местоположении персоны
                person_city[person] = new_city
        # сдвигаем текущий день
        cur_day = next_change

    # После всех интервалов и применений событий — готово. Нужно вывести города с ненулевыми днями,
    # отсортированные по алфавиту (обычный порядок символов: ABC...Zabc...z)
    # Но в задаче сказано: "Если таких дней не было, пропустите этот город."
    # Значит выводим только города, у которых city_days[city] > 0.

    # Подготовим список городов: те, которые есть в city_days с >0
    output_cities = [c for c, d in city_days.items() if d > 0]
    output_cities.sort()  # лексикографическая сортировка по инструкции

    out_lines = []
    for c in output_cities:
        out_lines.append(f"{c} {city_days[c]}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()

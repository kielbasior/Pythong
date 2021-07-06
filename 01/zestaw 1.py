import itertools
"""
#zad 1
for x in range(100, 1000):
  liczby = [int(x) for x in str(x)]
  if liczby[2] > liczby[1] and liczby[1] > liczby[0]:
    print(x)

#zad 2
polish_digits = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]
english_digits = ["a", "c", "e", "l", "n", "o", "s", "z", "z"]
def zad1(string):
    for x in range(len(string)):
        for y in range(len(polish_digits)):
            if string[x].lower() == polish_digits[y].lower():
                string = string.replace(string[x], english_digits[y])
    return string
print(zad1("Szczęście jest tak bardzo blisko"))
"""
#zad 3
slowa = ["korniszon", "maciek", "serdelki", "masło"]
def pary(list):
    for x in range(len(list)):
        new_item = (list[x], len(list[x]))
        list.remove(list[x])
        list.insert(x, new_item)
    return list
print(pary(slowa))

#zad 4
dates = [{'d': 4, 'm': 10, 'y': 2000},
        {'d': 2, 'm': 11, 'y': 2001},
        {'d': 10, 'm': 9, 'y': 2000},
        {'d': 4, 'm': 5, 'y': 2000},
        {'d': 5, 'm': 3, 'y': 2001},
        {'d': 6, 'm': 1, 'y': 2000},
        {'d': 2, 'm': 5, 'y': 2000},
        {'d': 1, 'm': 2, 'y': 2001},
        {'d': 10, 'm': 9, 'y': 2000}]

sorted_days = sorted(dates, key=lambda d: d['d'])
sorted_months = sorted(sorted_days, key=lambda d: d['m'])
sorted_dates = sorted(sorted_months, key=lambda d: d['y'])
print(sorted_dates)

#zad 5
lista = [[1, 2, 3], ["Abba", "aff"], [-2, 4, 5]]

flattened_list = list(itertools.chain(*lista))
print(flattened_list)










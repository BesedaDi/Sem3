class Packal_list:
    def __init__(self, list_python):
        self.spisok = list_python

    def __setitem__(self, key, value):
        self.spisok[key] = value

    def __getitem__(self, item):
        return self.spisok[item-1]

    def __str__(self):
        return self.spisok

a = Packal_list([1, 2, 3])
print(a[1])

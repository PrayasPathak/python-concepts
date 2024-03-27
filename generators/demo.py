def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


custom_for((1, 2, 3, 4, 5))


class Genarator:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if Genarator.current < self.last:
            num = Genarator.current
            Genarator.current += 1
            return num
        raise StopIteration


gen = Genarator(0, 100)
for i in gen:
    print(i)

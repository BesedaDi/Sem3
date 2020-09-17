class Carbase:
    def __init__(self, car_type, photo_le_name, brand, carrying):
        self.car_type = car_type
        self.photo_le_name = photo_le_name
        self.brand = brand
        self.carrying = carrying

    def photo_le_ext(self):
        rsh = list(self.photo_le_name.split('.'))[1]

        return rsh


class Car(Carbase):
    def __init__(self, car_type, photo_le_name, brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_le_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count

    def __str__(self):
        return '{} {} {} {}   {}  '.format(self.car_type, self.brand, self.passenger_seats_count,
                                                self.photo_le_name, self.carrying)


class Truck(Carbase):
    def __init__(self, car_type, photo_le_name, brand, carrying, body_whl):
        super().__init__(car_type, photo_le_name, brand, carrying)
        self.body_whl = body_whl
        self.body_width, self.body_height, self.body_lenght = map(float, body_whl.split('x'))

    def __str__(self):
        return '{} {}   {} {} {}  '.format(self.car_type, self.brand, self.photo_le_name, self.body_whl,
                                                 self.carrying)

    def get_body_volume(self):
        return float(self.body_width) * float(self.body_height) * float(self.body_lenght)


class Specmachine(Carbase):
    def __init__(self, car_type, photo_le_name, brand, carrying, extra):
        super().__init__(car_type, photo_le_name, brand, carrying)
        self.extra = extra

    def __str__(self):
        return '{} {}   {}   {} {}'.format(self.car_type, self.brand, self.photo_le_name, self.carrying, self.extra)


def get_car_list(filename):
    car_list = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line != '':
            try:
                if line[0] != 'spec_machine':
                    car_type, brand, passenger_seats_count, photo_le_name, body_whl, carrying = map(str, line.split(', '))
                else:
                    car_type, brand, passenger_seats_count, photo_le_name, body_whl, carrying, extra = map(str, line.split(', '))

                if car_type in ['car', 'truck', 'spec_machine']:
                    if car_type == 'car':
                        # passenger_seats_count = int(line[2])
                        car_list.append(Car(car_type, photo_le_name, brand, carrying, passenger_seats_count))
                    elif car_type == 'truck':
                        # body_whl = line[4]
                        body_width, body_height, body_lenght = map(float, body_whl.split('x'))
                        car_list.append(Car(car_type, brand, photo_le_name, body_whl, carrying))
                    elif car_type == 'truck':
                        # extra = line[6]
                        car_list.append(Car(car_type, photo_le_name, brand, carrying, extra))
                else:
                    continue
            except IndexError:
                continue
            except TypeError:
                continue
            line = f.readline()
    return car_list

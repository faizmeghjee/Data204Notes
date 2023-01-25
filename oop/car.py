# %%
class Window:

    def __init__(self, tint: str = '', thickness: str = '', material: str = '') -> None:
        self.tint = tint
        self.thickness = thickness
        self.material = material   

class Door(Window):

    def __init__(self, open_style: str = '', lock_type: str = '', handle: str = '', tint: str = '', thickness: str = '', material: str = '') -> None:
        super().__init__(tint, thickness, material)
        self.open_style = self.set_open_style(open_style)
        self.lock_type = self.set_lock_type(lock_type)
        self.handle = self.set_handle(handle)
    
    def get_door_details(self):
        print('Open Style: ' + str(self.open_style))
        print('Lock Type: ' + str(self.lock_type))
        print('Handle Type: ' + str(self.handle))

    def open(self):
        return print('Door is now open')

    def shut(self):
        return print('Door is now shut')

    def lock_door(self):
        return print('Door is locked')

    def wind_window_down(self):
        return print('Window is down')

    def set_open_style(self, open_style):
        open_styles = ['standard', 'vertical']
        if open_style.lower() in open_styles:
            self.open_style = open_style.lower()
            return self.open_style
        if open_style == '':
            pass
        else:
            return print('Open style unavailable, please choose either:\nstandard or verical\n')

    def set_lock_type(self, lock_type):
        lock_types = ['remote', 'manual']
        if lock_type.lower() in lock_types:
            self.lock_type = lock_type.lower()
            return self.lock_type
        if lock_type == '':
            pass
        else:
            return print('Lock type unavailable, please choose either:\nremote or manual\n')

    def set_handle(self, handle):
        handles = ['plastic', 'metal']
        if handle.lower() in handles:
            self.handle = handle.lower()
            return self.handle
        if handle == '':
            pass
        else:
            return print('Handle unavailable, please choose either:\nplastic or metal\n')


class Car(Door):

    def __init__(self, make: str = '', style: str = '', colour: str = '', doors: str = '', open_style: str = '', lock_type: str = '', handle: str = '', tint: str = '', thickness: str = '', material: str = '') -> None:
        super().__init__(open_style, lock_type, handle, tint, thickness, material)
        self.make = self.set_make(make)
        self.style = self.set_style(style)
        self.colour = self.set_colour(colour)
        self.doors = self.set_doors(doors)

    def get_car_details(self):
        print('Car Make: ' + str(self.make))
        print('Style: ' + str(self.style))
        print('Colour: ' + str(self.colour))
        print('Doors: ' + str(self.doors))

    def accelerate(self):
        return print(f'{self.make} is accelerating')

    def brake(self):
        return print('Errrrrrrr')

    def steer(self):
        return print(f'{self.make} is turning')

    def park(self):
        return print(f'{self.make} is now parked')

    def set_colour(self, colour: str):
        colours = ['red', 'silver', 'black']
        if colour.lower() in colours:
            self.colour = colour.lower()
            # print(f'Colour has been set to {self.colour}')
            return self.colour
        if colour == '':
            pass
        else:
            return print("Colour isn't available \nPlease choose either:\nred, silver or black\n")

    def set_style(self, style):
        styles = ['hatchback', 'cruiser', 'sport']
        if style.lower() in styles:
            self.style = style.lower()
            # print(f'Style has been set to {self.style}\n')
            return self.style
        if style == '':
            pass
        else:
            return print("Style isn't available \nPlease choose either:\nhatchback, cruiser or sport\n")

    def set_doors(self, doors):
        door_options = ['3 door', '5 door']
        if doors.lower() in doors:
            self.doors = doors.lower()
            # print(f'{self.make} is now a {self.doors}\n')
            return self.doors
        elif doors == '':
            return
        else:
            return print("Door option isn't available \nPlease choose either:\n3 door or 5 door\n")

    def set_make(self, make):
        makes = ['Honda', 'Toyota', 'Porsche']
        if make.title() in makes:
            self.make = make.title()
            # print(f'Car is now a {self.make}')
            return self.make
        if make == '':
            return
        else:
            return print("Car option isn't available \nPlease choose either:\nHonda, Toyota or Porsche\n")


car1 = Car()
car1.get_car_details()

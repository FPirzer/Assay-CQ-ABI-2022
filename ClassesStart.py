class bike:
    def __init__(
        self, arg_brand, arg_nr_sprockets, arg_nr_pinion, arg_sprocket, arg_pinion
    ):
        self.__brand = str(arg_brand)
        self.__nr_sprockets = int(arg_nr_sprockets)
        self.__nr_pinions = int(arg_nr_pinion)
        self._sprockets = int(arg_sprocket)
        self._pinions = int(arg_pinion)

    def get_brand(self):
        return self.__brand

    def get_nrsprockets(self):
        return self.__nr_sprockets

    def get_nrpinions(self):
        return self.__nr_pinions

    def get_sprockets(self):
        return self._sprockets

    def get_pinions(self):
        return self._pinions

    def up_sprocket(self):
        if self._sprockets < self.__nr_sprockets:
            self._sprockets += 1
        else:
            print("Already in the highest sprocket.")

    def down_sprocket(self):
        if self._sprockets > 1:
            self._sprockets -= 1
        else:
            print("Already in the lowest sprocket.")

    def up_pinion(self):
        if self._pinions < self.__nr_pinions:
            self._pinions += 1
        else:
            print("Already in the highest pinion.")

    def down_pinion(self):
        if self._pinions > 1:
            self._pinions -= 1
        else:
            print("Already in the lowest pinion.")

    def gear_status(self):
        return f"Pinions are at {self._pinions} and sprockets are at {self._sprockets}"


BMX = bike("mountainbike", 3, 5, 2, 4)
print(BMX._pinions)
print(BMX.get_brand())
print(BMX.gear_status())
BMX.down_pinion()
BMX.down_pinion()
BMX.down_pinion()
BMX.down_pinion()
BMX.up_pinion()
BMX.up_pinion()
BMX.up_pinion()
BMX.up_pinion()
BMX.up_pinion()

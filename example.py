class Base(object):
    def __init__(self, *args, data=None, **kwargs):
        print("Data is : ", data)
        print("Kwargs are : ", kwargs)


class MyBaseObject(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MyObjects(MyBaseObject):
    def __init__(self, *args, game=None, **kwargs):
        super().__init__(*args, **kwargs)
        print("Game is ", game)
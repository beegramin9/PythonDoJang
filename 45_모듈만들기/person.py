class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'안녕하세요. 저는 {self.address}에 사는 {self.age}살 {self.name}입니다.')

from dataclasses import dataclass


@dataclass
class Road:
    __length: int = None
    __width: int = None

    def calculate(self, weight: int, thickness: int = 1):
        return f"{round((self.__length * self.__width * weight * thickness) / 1000)} Т"


def main():
    roadClass = Road(20, 5000)
    print(roadClass.calculate(25, 5))


if __name__ == '__main__':
    main()

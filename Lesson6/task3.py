
class Worker:
    name: str = None
    surname: str = None
    position: str = None
    _income: dict = None

    def __init__(self,name:str,surname:str,position:str,wage:int,bonus:int)->None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
            }



class Position(Worker):
    def get_full_name(self):
        return f"{self.name}  {self.surname}"

    def get_total_income(self):
        return self._income['wage']+self._income['bonus']

def main():
    name, surname, position, wage, bonus=['Дмитрий','Фёдоров','Вратарь',19334,2453]
    positionClass = Position(name, surname, position, wage, bonus)
    print(f"name variable:{name}  name attribute: {positionClass.name}")
    print(f"surname variable:{surname}  surname attribute: {positionClass.surname}")
    print(f"position variable:{position}  position attribute: {positionClass.position}")
    print(f"full name: {positionClass.get_full_name()}")
    print(f"Total income: {positionClass.get_total_income()}")

if __name__ == '__main__':
    main()

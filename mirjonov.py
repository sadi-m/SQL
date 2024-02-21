from genericpath import samefile
import json

from auto_info import *
from typing import List



def load_AutoTypedDict(filename: str) -> List[AutoInfoTypedDict]:
    with open(filename, mode='r') as f:
        data = json.load(f)
        
    return [TypedDict_from_dict(item) for item in data]

def save_AutoTypedDict(data: List[AutoInfoTypedDict], filename:str):
    
    data = [TypedDict_to_dict(item) for item in data]
    with open(filename, mode='w') as f:
        json.dump(data, f)

def read_Auto_infoTypedDict() -> AutoInfoTypedDict:
    surname = input('Фамилия владельца: ')
    code_mark_auto = int (input('Код марки автомобиля: '))
    mark_auto = input('Марка автомобиля: ')
    fuel = int (input('Марка топлива: '))
    engine_power = input('Мощность двигателя: ')
    tank_volume = input('Объем бака: ')
    gasoline_remaining = input('Остаток бензина: ')
    oil_volume = input('Объем масла: ')
    return AutoInfoTypedDict(surname=surname, code_mark_auto=code_mark_auto, mark_auto=mark_auto, fuel=fuel,
                             engine_power=engine_power,tank_volume=tank_volume,gasoline_remaining=gasoline_remaining,oil_volume=oil_volume)

def load_Auto(filename: str, Auto: AutoInfo | AutoInfoNamedTuple) -> List[AutoInfo] | List[AutoInfoNamedTuple]:
    with open(filename, mode='r') as f:
        data = json.load(f)
        
    return [Auto.from_dict(item) for item in data]

def save_Auto(data: List[AutoInfo] | List[AutoInfoNamedTuple], filename:str):
    
    data = [item.to_dict() for item in data]
    with open(filename, mode='w') as f:
        json.dump(data, f)

def read_Auto_info(Auto: AutoInfo | AutoInfoNamedTuple) -> List[AutoInfo] | List[AutoInfoNamedTuple]:
    surname = input('Фамилия владельца: ')
    code_mark_auto = int (input('Код марки автомобиля: '))
    mark_auto = input('Марка автомобиля: ')
    fuel = int (input('Марка топлива: '))
    engine_power = input('Мощность двигателя: ')
    tank_volume = input('Объем бака: ')
    gasoline_remaining = input('Остаток бензина: ')
    oil_volume = input('Объем масла: ')
    return Auto(surname, code_mark_auto, mark_auto, fuel, engine_power, tank_volume, gasoline_remaining, oil_volume)


if __name__ == "__main__":
    Auto_one = AutoInfoTypedDict(surname='Dallas', code_mark_auto=1117, mark_auto='VAZ Lada Kalina', fuel=92,
                                 engine_power=81, tank_volume=50, gasoline_remaining=25, oil_volume=3.1)
    Auto_two = AutoInfoTypedDict(surname='Korben', code_mark_auto=2015, mark_auto='KIA Rio', fuel=92,
                                 engine_power=100, tank_volume=43, gasoline_remaining=10, oil_volume=3.5)
    Auto_three = AutoInfoTypedDict(surname='Mirjonov', code_mark_auto=2109, mark_auto='Vaz', fuel=92,
                                 engine_power=78, tank_volume=39, gasoline_remaining=20, oil_volume=4)
    data = [Auto_one, Auto_two, Auto_three]
    
    save_AutoTypedDict(data, 'data.json')
    data_copy = load_AutoTypedDict('data.json')

    for element in data_copy:
        print(element)
    
    new_Auto = read_Auto_infoTypedDict()
    print(new_Auto)

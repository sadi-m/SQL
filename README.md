# SQL
A database is like a virtual warehouse where information is stored in an organized manner. 
from auto_info import *


def format_auto_info(auto: AutoInfo | AutoInfoNamedTuple) -> str:
    """Formats auto info to string"""
    return (f"Фамилия: {auto.surname}\n"
            f"Код марки: {auto.code_mark_auto}\n"
            f"Марка авто: {auto.mark_auto}\n"
            f"Топливо: {auto.fuel}\n"
            f"Мощность двигателя: {auto.engine_power} л\с\n"
            f"Объем бака: {auto.tank_volume} л\n"
            f"Остаток бензина: {auto.gasoline_remaining} л\n"
            f"Объем масла: {auto.oil_volume} л\n")

def format_auto_info_typeddict(auto: AutoInfoTypedDict) -> str:
    """Formats auto info from TypedDict to string"""
    return (f"Фамилия: {auto['surname']}\n"
            f"Код марки: {auto['code_mark_auto']}\n"
            f"Марка авто: {auto['mark_auto']}\n"
            f"Топливо: {auto['fuel']}\n"
            f"Мощность двигателя: {auto['engine_power']} л\с\n"
            f"Объем бака: {auto['tank_volume']} л\n"
            f"Остаток бензина: {auto['gasoline_remaining']} л\n"
            f"Объем масла: {auto['oil_volume']} л\n")


if __name__ == "__main__":
    auto = AutoInfo('Mirjonov', 2109, 'Vaz', 92, 78, 39, 20, 4)
    print(format_auto_info(auto))
    auto = AutoInfoTypedDict(surname='Mirjonov', code_mark_auto=2109, mark_auto='Vaz', fuel=92 , engine_power=78, tank_volume=39, gasoline_remaining=20, oil_volume=4)
    print(format_auto_info_typeddict(auto))

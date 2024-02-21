import argparse
from json import load

from auto_find import *
from auto_formatter import *
from auto_info import *
from auto_insert_delete import *
from auto_io import *


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--create", type=str, help="create empty data file")
    group.add_argument("-i", "--insert", type=str, help="insert data")
    group.add_argument("-d", "--delete", type=str, help="delete data")
    group.add_argument("-f", "--findname", type=str, help="find auto by name")
    group.add_argument("-p", "--print", type=str, help="print data")
    parser.add_argument("-t", "--type", type=str, help="choise type", default='dc')
    args = parser.parse_args()
    print(args)

    if args.create:
        if args.type == 'nt':
            save_Auto([], args.create)
        elif args.type == 'td':
            save_AutoTypedDict([], args.create)
        else:
            save_Auto([], args.create)
    
    elif args.insert:
        if args.type == 'nt':
            data = load_Auto(args.insert, AutoInfoNamedTuple)
            inserted_auto = read_Auto_info(AutoInfoNamedTuple)
            try:
                data = insert_AutoInfo(data, inserted_auto)
            except InsertionError:
                print('Вставляю что-то не так!')
            finally:
                save_Auto(data, args.insert)
        elif args.type == 'td':
            data = load_AutoTypedDict(args.insert)
            inserted_auto = read_Auto_infoTypedDict()
            try:
                data = insert_AutoInfoTypedDict(data, inserted_auto)
            except InsertionError:
                print('Вставляю что-то не так!')
            finally:
                save_AutoTypedDict(data, args.insert)
        else:
            data = load_Auto(args.insert, AutoInfo)
            inserted_auto = read_Auto_info(AutoInfo)
            try:
                data = insert_AutoInfo(data, inserted_auto)
            except InsertionError:
                print('Вставляю что-то не так!')
            finally:
                save_Auto(data, args.insert)
    
    elif args.delete:
        if args.type == 'nt':
            data = load_Auto(args.delete, AutoInfoNamedTuple)
            deleted_auto = read_Auto_info(AutoInfoNamedTuple)
            try:
                data = delete_AutoInfo(data, deleted_auto)
            except DeletionError:
                print('Удаляю что-то неправильное!')
            finally:
                save_Auto(data, args.delete)
        elif args.type == 'td':
            data = load_AutoTypedDict(args.delete)
            deleted_auto = read_Auto_infoTypedDict()
            try:
                data = delete_AutoInfoTypedDict(data, deleted_auto)
            except DeletionError:
                print('Удаляю что-то неправильное!')
            finally:
                save_AutoTypedDict(data, args.delete)
        else:
            data = load_Auto(args.delete, AutoInfo)
            deleted_auto = read_Auto_info(AutoInfo)
            try:
                data = delete_AutoInfo(data, deleted_auto)
            except DeletionError:
                print('Удаляю что-то неправильное!')
            finally:
                save_Auto(data, args.delete)
    
    elif args.findname:
        Auto_name = input('Name to find: ')
        Typed = input('Typed to find: ')
        if args.type == 'nt':
            data = load_Auto(args.findname, AutoInfoNamedTuple)
            if Typed == 'surname':
                results = find_by_surname_NT(data, Auto_name)
            elif Typed == 'code_mark_auto':
                results = find_by_code_mark_auto_NT(data, int(Auto_name))
            else:
                results = find_by_engine_power_NT(data, Auto_name)
        elif args.type == 'td':
            data = load_AutoTypedDict(args.findname)
            if Typed == 'surname':
                results = find_by_surname_TD(data, Auto_name)
            elif Typed == 'code_mark_auto':
                results = find_by_code_mark_auto_TD(data, int (Auto_name))
            else:
                results = find_by_engine_power_TD(data, Auto_name)
        else:
            data = load_Auto(args.findname)
            if Typed == 'surname':
                results = find_by_surname(data, Auto_name)
            elif Typed == 'code_mark_auto':
                results = find_by_code_mark_auto(data, int(Auto_name))
            else:
                results = find_by_engine_power(data, Auto_name)
        if results:
            if args.type == 'td':
                for item in results:
                    print(format_auto_info_typeddict(item))
            else:
                for item in results:
                    print(format_auto_info(item))
        else:
            print('Нет автоматической информации с таким именем!')
    
    elif args.print:
        if args.type == 'nt':
            data = load_Auto(args.print, AutoInfoNamedTuple)
        elif args.type == 'td':
            data = load_AutoTypedDict(args.print)
        else:
            data = load_Auto(args.print, AutoInfo)
        if data:
            if args.type == 'td':
                for item in data:
                    print(format_auto_info_typeddict(item))
            else:
                for item in data:
                    print(format_auto_info(item))

    else:
        print('Неизвестная команда!')

if __name__ == "__main__":
    main()

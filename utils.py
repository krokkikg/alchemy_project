from database.manager import StudentGroupManager

from db import get_session
from os import system

session = get_session()


def clear_terminal():
    system("clear")





def add_new_group():
    name = input("Введите пожалуйста название новой группы:")
    group_manager = StudentGroupManager(session=session)
    group_manager.insert_group({"name":name})
    clear_terminal()
    print("Новая группа успешно добавлена!")


def get_groups():
    manager = StudentGroupManager(session)
    result=manager.get_all_groups()
    print("Все группы: ")
    for group in result:
        print(f"{group.id}- {group.name}")




def search_group():
    manager = StudentGroupManager(session)
    search_name = input("введите имя для поиска: ")
    group_list=manager.search_by_group_name(search_name)
    if group_list:
        for group in group_list:
            print(f"{group.id} - {group.name}")
    else:
        print("Групп с таким названием не найдено!")

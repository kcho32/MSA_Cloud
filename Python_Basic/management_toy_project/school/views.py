from school.exception import DuplicateError
from school.exception import NotFoundError
from .file_registry import init_data_load, save_file

people = []

def register(person):
    #ID는 UNIQUE하기 떄문에 중복 check를 해서 exception 발생
    #중복시 DuplicateError
    index = is_exist(person.id)
    if index > -1:
        raise DuplicateError(person.id)
    else:
        people.append(person)


def update(person):
    #id check를 해서 exception 발생
    #없을시 NotFoundError
    index = is_exist(person.id)
    if index == -1:
        raise NotFoundError(person.id)
    else:
        people[index] = person

def remove(id):
    #id check를 해서 exception 발생
    #없을시 NotFoundError
    index = is_exist(id)
    if index == -1:
        raise NotFoundError(id)
    else:
        people.pop(index)


def get_person(id):
    #id check를 해서 exception 발생
    #없을시 NotFoundError
    index = is_exist(id)
    if index == -1:
        raise NotFoundError(id)
    else:
        return people[index]


def get_all_people():
    return people


def is_exist(id):
    for index, person in enumerate(people):
        if person.id == id:
            return index
    return -1


def save_list():
    save_file(people)


def load_list():
    init_data_load()
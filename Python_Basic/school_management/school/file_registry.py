from . import views
from . import models
import os.path

def save_file(people):
    save_file = open("management_toy_project/list.dat",'w')
    for index, p in enumerate(views.people):
        if isinstance(p, models.Student):
            save_file.write("1, {0}, {1}, {2}\n".format(p.id, p.name, p.major))
        elif isinstance(p, models.Instructor):
            save_file.write("2, {0}, {1}, {2}\n".format(p.id, p.name, p.subject))
        elif isinstance(p, models.Employee):
            save_file.write("3, {0}, {1}, {2}\n".format(p.id, p.name, p.department))
    save_file.close()


def init_data_load():
    fileExist = os.path.isfile("management_toy_project/list.dat")
    people = []
    if fileExist:
        read_file = open("management_toy_project/list.dat",'r')
        while True:
            data = read_file.readline().strip("\n")
            data_list = data.split(",")
            
            if data_list[0] == "1":
                person = models.Student(data_list[1], data_list[2], data_list[3])
            elif data_list[0] == "2":
                person = models.Instructor(data_list[1], data_list[2], data_list[3])
            elif data_list[0] == "3":
                person = models.Employee(data_list[1], data_list[2], data_list[3])
            people.append(person)
            if not data: break
        read_file.close()
        return people
    
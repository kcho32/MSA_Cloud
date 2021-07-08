from . import views
from . import models

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
    load_file = open("management_toy_project/list.dat",'r')
    
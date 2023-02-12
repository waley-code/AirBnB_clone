#!/usr/bin/python3
"""
This is the console module which contains the HBNBCommand class
"""
import cmd
from importlib import import_module
from models import storage
from ast import literal_eval


class HBNBCommand(cmd.Cmd):
    """This is a simple command interpreter

    Attributes:
        prompt (str): used to query for the next command
        models (tuple): all the classes that exist for this project
        data (dict): all objects that exist in the json file
        cls_dicts (dict): all classes with their respective module name
    """
    prompt = "(hbnb) "
    __models = ('BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                'Review')
    __data = storage.all()
    __cls_dicts = {'BaseModel': "base_model", 'User': "user",
                   'State': "state", 'City': "city", 'Amenity': "amenity",
                   'Place': "place", 'Review': "review"}

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def precmd(self, line):
        """Handle command line input and parse it if necessary"""
        if "." in line and "(" in line:
            if "{" not in line:
                args = line.replace("(", ",").strip(")").split(",")
                cm_str = args.pop(0).split(".")
                cls_name = cm_str[0]
                cm = cm_str[1]
                last = ""
                if len(args) >= 1:
                    last = args[:]
                if len(last) == 1:
                    last = last[0].strip('"')
                elif len(last) == 3:
                    last = [x.replace('"', "") for x in last]
                    last = f'{last[0]} {last[1]} {last[2]}'
                    last = last.replace(",", "")
                else:
                    pass
            else:
                args = line.replace("(", " ").strip(")")
                i = args.find("{")
                diction = args[i:]
                args = args[: i - 2].split(".")
                cls_name = args[0]
                str_li = args[1].split()
                cm, ins_id = str_li[0], str_li[1].replace('"', "")
                last = f'{ins_id} {diction}'
            line = f'{cm} {cls_name} {last}'
        return line

    def emptyline(self):
        """Do nothing when an empty line is passed"""
        pass

    def do_create(self, line):
        """creates a new instance of any of the existing Classes for this
        project, saves it to the JSON file and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.__models:
            print("** class doesn't exist **")
        else:
            line = line.strip()
            f_name = f'models.{self.__cls_dicts[line]}'
            module = import_module(f_name)
            Class = getattr(module, line)
            my_model = Class()
            storage.new(my_model)
            storage.save()
            print(my_model.id)

    def do_show(self, line):
        """prints the string representation of an instance based on
        the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        line = line.strip()
        args = line[:].split()
        if args[0] not in self.__models:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")

        else:
            obj_key = line[:].replace(" ", ".")
            for key, value in self.__data.items():
                if key == obj_key:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """deletes an instance based on the class name and id then
        saves the change into the JSON file
        """
        if not line:
            print("** class name missing **")
            return
        line = line.strip()
        args = line[:].split()
        if args[0] not in self.__models:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")

        else:
            obj_key = line[:].strip().replace(" ", ".")
            for key in self.__data.keys():
                if key == obj_key:
                    del self.__data[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """prints all string representation of all instances based
        or not on the class name
        """
        str_rep = []
        line = line.strip()
        if line and line in self.__models:
            for key, value in self.__data.items():
                if key.split(".")[0] == line:
                    str_rep.append(str(value))
        elif line and line not in self.__models:
            print("** class doesn't exist **")
            return
        else:
            for value in self.__data.values():
                str_rep.append(str(value))

        print(str_rep)

    def do_update(self, line):
        """updates an instance based on the class name and id by adding
        or updating atrribute then save the change into the JSON file
        """
        dont = ('id', 'updated_at', 'created_at')
        line = line.strip()
        args = line[:].split()
        size = len(args)
        if size == 0:
            print("** class name missing **")
            return
        elif size == 1:
            if args[0] not in self.__models:
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        if size == 2:
            if args[0] not in self.__models:
                print("** class doesn't exist **")
                return
            keys = self.__data.keys()
            if f'{args[0]}.{args[1]}' not in keys:
                print("** no instance found **")
                return
            print("** attribute name missing **")
            return
        elif size == 3:
            if args[0] not in self.__models:
                print("** class doesn't exist **")
                return
            keys = self.__data.keys()
            if f'{args[0]}.{args[1]}' not in keys:
                print("** no instance found **")
                return
            print("** value missing **")
            return
        else:
            if args[0] not in self.__models:
                print("** class doesn't exist **")
                return
            keys = self.__data.keys()
            if f'{args[0]}.{args[1]}' not in keys:
                print("** no instance found **")
                return

        cls_name = args[0]
        ins_id = args[1]
        if "{" in args[2]:
            i = line.find('{')
            string = line[i:]
            dic_t = literal_eval(string)
        else:
            dic_t = {args[2]: args[3]}

        get_key = f'{cls_name}.{ins_id}'
        dic = self.__data[get_key].to_dict()
        for key, value in dic_t.items():
            value = value.strip('"\'')
            if key in dic.keys():
                value = type(dic[key])(value)
            else:
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        value = str(value)
            dic_t.update({key: value})
        dic.update(dic_t)
        f_name = f'models.{self.__cls_dicts[cls_name]}'
        module = import_module(f_name)
        Class = getattr(module, cls_name)
        storage.new(Class(**dic))
        storage.save()

    def do_count(self, line):
        """print number of instances of a class"""
        count = 0
        line = line.strip()
        for key in self.__data.keys():
            if key.split(".")[0] == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

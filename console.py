#!/usr/bin/python3
"""
This is the console module which contains the HBNBCommand class
"""
import cmd
from importlib import import_module
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is a simple command interpreter

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
        """
        exit the console
        """
        return True

    def do_EOF(self, line):
        """
        exit the console
        """
        return True

    def do_create(self, line):
        """
        creates a new instance of any of the existing Classes for this
        project, saves it to the JSON file and prints the id
        """
        line = line.strip()
        if not line:
            print("** class name missing **")
        elif line not in self.__models:
            print("** class doesn't exist **")
        else:
            f_name = f'models.{self.__cls_dicts[line]}'
            module = import_module(f_name)
            Class = getattr(module, line)
            my_model = Class()
            storage.new(my_model)
            storage.save()
            print(my_model.id)

    def do_show(self, line):
        """
        prints the string representation of an instance based on the class
        name and id
        """
        if not line:
            print("** class name missing **")
            return
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
        """
        deletes an instance based on the class name and id then saves
        the change into the JSON file
        """
        if not line:
            print("** class name missing **")
            return
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
        """
        prints all string reprensation of all instances based or not on
        the class name
        """
        str_rep = []
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
        """
        updates an instance based on the class name and id by adding or
        updating atrribute then save the change into the JSON file
        """
        dont = ('id', 'updated_at', 'created_at')
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
            c = self.__data.values()
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
        atr_name = args[2]
        atr_val = args[3]
        if atr_name in dont:
            return
        atr_val = atr_val.strip('"\'')
        for key, value in self.__data.items():
            check = key.split('.')
            if check[0] == cls_name and check[1] == ins_id:
                dic = value.to_dict()
                if atr_name in dic.keys():
                    atr_val = type(dic[atr_name])(atr_val)
                else:
                    try:
                        atr_val = int(atr_val)
                    except ValueError:
                        try:
                            atr_val = float(atr_val)
                        except ValueError:
                            atr_val = str(atr_val)
                dic.update({atr_name: atr_val})
                cls_name = dic['__class__']
                f_name = f'models.{self.__cls_dicts[cls_name]}'
                module = import_module(f_name)
                Class = getattr(module, cls_name)
                storage.new(Class(**dic))
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

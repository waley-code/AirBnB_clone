#!/usr/bin/python3
import cmd
import importlib
from models import storage
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __models = ('BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review')
    __data = storage.all()
    __s = {'BaseModel': "base_model", 'User': "user",'State': "state",
           'City':"city", 'Amenity': "amenity",
           'Place':"place", 'Review':"review"}
    """
    An empty line + enter shouldn't execute anything

    """
    
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
        line = line.strip()
        if not line:
            print("** class name missing **")
        elif line not in self.__models:
            print("** class doesn't exist **")
        else:
            module = importlib.import_module(f'models.{self.__s[line]}')
            Class = getattr(module, line)
            my_model = Class()
            storage.new(my_model)
            storage.save()
            print(my_model.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return
        d = line[:].split()
        if d[0] not in self.__models:
            print("** class doesn't exist **")
        elif len(d) != 2:
            print("** instance id missing **")

        else:
            c = line[:].replace(" ", ".")
            for key, value in self.__data.items():
                if key == c:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self,line):
        if not line:
            print("** class name missing **")
            return
        d = line[:].split()
        if d[0] not in self.__models:
            print("** class doesn't exist **")
        elif len(d) != 2:
            print("** instance id missing **")

        else:
            c = line[:].strip().replace(" ", ".")
            for key in self.__data.keys():
                if key == c:
                    del self.__data[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        out = []
        if line and line in self.__models:
             for key, value in self.__data.items():
                if key.split(".")[0] == line:
                    out.append(str(value))
        elif line and line not in self.__models:
            print("** class doesn't exist **")
            return
        else:
            for value in self.__data.values():
                out.append(str(value))

        print(out)

    def do_update(self, line):
        dont = ('id', 'updated_at', 'created_at')
        out = []
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

        cls_name, id, ki, val = args[0], args[1], args[2], args[3]
        if ki in dont:
            return
        val = val.strip('"')
        for key, value in self.__data.items():
            check = key.split('.')
            if check[0] == cls_name and check[1] == id:
                dic = value.to_dict()
                if ki in dic.keys():
                    if type(dic[ki]) == str:
                        val = str(val)
                    elif type(dic[ki]) == int:
                        val = int(val)
                    elif type(dic[ki]) == float:
                        val = float(val)
                else:
                    try:
                        val = int(val)
                    except ValueError:
                        try:
                            val = float(val)
                        except ValueError:
                            val = str(val)
                dic.update({ki:val})
                cls_name = dic['__class__']
                module = importlib.import_module(f'models.{self.__s[cls_name]}')
                Class = getattr(module, cls_name)
                storage.new(Class(**dic))
                storage.save()


if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1:
        HBNBCommand().onecmd(' '.join(argv[1:]))
    else:
        HBNBCommand().cmdloop()

#!/usr/bin/python3
""" defines the entry point of command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'
    __cls = ["BaseModel"]

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        """Ctrl+D to exit the program"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__cls:
            print("**  class does not exist **")
        else:
            if args[0] == "BaseModel":
                inst = BaseModel()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        args = line.split(" ")
        if args[0] in __class__.__cls:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    if key == obj_id:
                        print(all_objs[obj_id])
                        break
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("**class name missing **")
        else:
            print("** class doesn't exist **")
            
    
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file
        """
        args = line.split(" ")
        if args[0] in __class__.__cls:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                objs_dict = storage.all()
                if objs_dict.pop(key, None) is None:
                    print("** no instance found **")
                else:
                    storage.save()
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
    def do_all(self, line):
        """
         Prints all string representation of all instances based or not on the class name
        """
        args = line.split(" ")
        if args[0] == "" or args[0] in __class__.__cls:
            str_obj = []
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                if args == [''] or obj_key.split(".")[0] == args[0]:
                    str_obj.append(str(all_objs[obj_key]))
            print(str_obj)
        else:
            print("** class doesn't exist **")
            
    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating 
        attribute (save the change into the JSON file)
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif not args[0] in __class__.__cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
            else:
                print("** no instance found **")           
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
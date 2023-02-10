#!/usr/bin/python3
""" defines the entry point of command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        """Ctrl+D to exit the program"""
        print()
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, args):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]
            
        if not c_name:
            print("** class name missing **")
            return
        
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        if not c_id:
            print("** instance id missing **")
            
        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")
            
    
    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]
            
        if not c_name:
            print("** class name missing **")
            return
        
        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        
        if not c_id:
            print("** instance id missing **")
            
        key = c_name + "." + c_id
        
        try:
            del(storage.all()[key])
            storage.save()
        except keyError:
            print("** no instance foune **")
            
  
      
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
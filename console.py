#!/usr/bin/python3
""" defines the entry point of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'
    __cls = ["BaseModel"]
    
    def do_quit(self,line):
        return True
    
    def do_EOF(self, line):
        """Ctrl+D to exit the program"""
        print()
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
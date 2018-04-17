#!/usr/bin/env python3


class Person(object):
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print('My name is ' + self.name)
    
    def print_parents(self):
        mother = input("Enter mother's name: ")
        father = input("Enter father's name: ")

        print("{}'s parents are {} and {}.".format(self.name, mother, father))
        self.fake_func()

    def fake_func(self):
        pass
    
    def print_sth(self):
        print("I'm here!")


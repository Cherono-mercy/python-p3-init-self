#!/usr/bin/env python3

class Dog:
    #Method Definition
    def __init__(self, name, breed = "Mutt"):
        self.name = name    #argument for the dog's name stored in a self.name attribute 
        self.breed = breed  #optional argument for the dog's breed stored in a self.breed attribute default to "Mutt"
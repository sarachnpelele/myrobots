from solution import SOLUTION
import constants as c 
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        
        self.parents = {}

        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION()
        
        
    def Evolve(self):
        for pop in range(c.populationSize):
            self.parents[pop].Evaluate("GUI")
        """
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        """
        
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
    
    def Print(self):
        print("p: ", self.parent.fitness, "| c: ", self.child.fitness)

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass
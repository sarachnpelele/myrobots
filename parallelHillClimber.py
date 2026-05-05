from solution import SOLUTION
import constants as c 
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("del brain*.nndf")
        #os.system("del fitness*.txt")

        for file in os.listdir():
            if file.startswith("fitness") and file[7:].split(".")[0].isdigit():
                os.remove(file)
        
        self.nextAvailableID = 0
        self.parents = {}
        self.fitnessMatrix = np.zeros((c.populationSize, c.numberOfGenerations))

        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
    
    
    
        
    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)

        for pop in range(c.populationSize):
            self.fitnessMatrix[pop, currentGeneration] = self.children[pop].fitness

        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key] = self.children[key]
    
    def Print(self):
        for key in self.parents:
            print(" ")
            print("Fitness:")
            print("Parent: ", self.parents[key].fitness)
            print("Child: ", self.children[key].fitness)
            print(" ")


    def Show_Best(self):
        best = max(self.parents, key= lambda x: self.parents[x].fitness)
        self.parents[best].Start_Simulation("GUI") 
        print(" ")
        print("Best fitness: ", self.parents[best].fitness)
        print(" ")

    def Evaluate(self, solutions):
        
        for pop in range(c.populationSize):
            solutions[pop].Start_Simulation("DIRECT")

        
        for pop in range(c.populationSize):
            solutions[pop].Wait_For_Simulation_To_End()
        
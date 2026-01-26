import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")

num_rows = 5       
num_cols = 5       
tower_height = 10      

for row in range(num_rows):
    for col in range(num_cols):
        
        length = 1
        width  = 1
        height = 1

        x = col 
        y = row 
        z = height / 2   

        for i in range(tower_height):
            pyrosim.Send_Cube( name=f"Box_{row}_{col}_{i}",pos=[x, y, z],size=[length, width, height] )
            z += height / 2
            length *= 0.9
            width  *= 0.9
            height *= 0.9
            z += height / 2

pyrosim.End()

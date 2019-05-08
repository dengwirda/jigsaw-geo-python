
def savemsh(name,mesh):
    """
    SAVEMSH: save a MSH obj. to file.
    
    """
 
    with open(name,"w") as file:
        for ip in mesh.point.coord:
            dstr = mesh.point.coord
            file.write()    

    return
    
    
    

print("adivina la palabra!")

letra = (input("Ingresa una letra: "))
print(letra)

#os.system("cls")
    

def read():
    data = []
    with open (("./DATA/data.txt"), "r") as f:
        for i, f in enumerate(f):
            print(i, f)


#correr ciclo
#agregar = [i for i in range(f) ]



def run():
    pass

if __name__ =="__main__":
    read()
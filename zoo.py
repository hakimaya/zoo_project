class animal:
    def __init__(self,name,habitat,species,age,poids=None):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.species = species
        self.poids = poids
        self.id = None
count = 1
animals = []        


donnees_initiales = [
    ("Simba","Savane","Lion",5,190),
    ("Nala","Jungle","Tigre",3,None),
    ("Melman","Savane","Girafe",7,800),
    ("Zara","Savane","Zebre",4,None),
    ("Bubbles","Aquatique","Poisson-clown",1,0.1),
    ("Rex","Aquatique","Crocodile",15,90),
    ("Dumbo","Savane","Elephant",10,4000),
    ("Kiara","Savane","Lion",2,150),
    ("Anna","Jungle","Panthere",6,60),
    ("Pingu","Aquatique","Pingouin",3,15),
    ("Alex","Savane","Lion",8,200),
    ("Gloria","Savane","Hippopotame",9,1500),
    ("Marty","Savane","Zebre",5,300),
    ("Skipper","Aquatique","Pingouin",4,16),
    ("Timon","Jungle","Suricate",2,1),
    ("Pumba","Jungle","Phacochere",3,80),
    ("Baloo","Jungle","Ours",6,250),
    ("Kaa","Jungle","Serpent",10,20),
    ("Bagheera","Jungle","Panthere",7,55),
    ("Shere Khan","Jungle","Tigre",9,190),
]
for name,habitat,species,age,poids in donnees_initiales:
    a = animal(name,habitat,species,age,poids)
    a.id = count
    animals.append(a)
    count += 1

print("Chargement de animaux.csv...")
lenG = len(animals)
print(lenG ,"animeaux charges.")
print()



def add():
    name = input("Nom: ")
    age = int(input("Age: "))
    habitat = input("Habitat: ")
    species = input("Especes: ")
    poids = input("Poids (optionnel, entree vide pour ignorer): ")
    if poids == "":
        poids = None
    else:
        poids = float(poids)
    return name,age,habitat,species,poids
    
while 1:
    print("=== Zoo Management ===")
    print("1. Ajoutez les animaux")
    print("2. Afficher les animaux")
    print("3. Modifier un animala")
    print("4. Supprimer un animal")
    print("5. Rechercher un animal")
    print("6. Statistiques")
    print("0. Quitter")
    choix = int(input("Choix >"))
    if choix == 1:
        print("Ajouter combien d'animeaux? (1 pour un seul)")
        nombre = int(input("Nombre >"))
        if nombre < 1:
            print("Veuillez entrez un nombre egale ou superieure de 1")
        else:
            for i in range(1,nombre+1):
                print("--- Animal ",i,"/",nombre," ---", sep="")
                name,age,habitat,species,poids = add()
                new_animal = animal(name,habitat,species,age,poids)
                new_animal.id = count
                animals.append(new_animal)
                print("Animal ajoute! (id ",count,")", sep="")
                count += 1
    elif choix == 2:
        print("1. Liste complete")
        print("2. Liste par nom")
        print("3. Trier par age")
        print("4. Filtrer par habitat")
        choix2 = int(input("choix >"))
        if choix2 == 1:
            print(f"{'Id':<5}{'Nom':10}{'Especes':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
            for a in animals:
                if a.poids is None:
                    a.poids = "N/A"
                print(f"{a.id:<5}{a.name:10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
            print()
        elif choix2 == 2:
            animals_trie = sorted(animals, key=lambda a: a.name.lower())
            print(f"{'Id':<5}{'Nom':10}{'Especes':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
            for a in animals_trie:
                if a.poids is None:
                    a.poids = "N/A"
                print(f"{a.id:<5}{a.name:10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
            print()
        elif choix2 == 3:
            animals_trie = sorted(animals, key=lambda a: a.age)
            print(f"{'Id':<5}{'Nom':10}{'Especes':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
            for a in animals_trie:
                if a.poids is None:
                    a.poids = "N/A"
                print(f"{a.id:<5}{a.name:10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
        elif choix2 == 4:
            habitat_inp = input("Habitat: ")
            how = 0
            for a in animals:
                if habitat_inp == a.habitat:
                    how += 1
            if how == 0:
                print("Aucun animal trouve.")
            else:
                print(f"{'id':<5}{'Nom':<10}{'Especes':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
                for a in animals:
                    if habitat_inp == a.habitat:
                        print(f"{a.id:<5}{a.name:<10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
            print()
    elif choix == 3:
        mdf = int(input("Id de l'animal a modifier: "))
        print("1. Modifier l'habitat")
        print("2. Modifier l'age")
        choix = int(input("Choix >"))
        if choix == 1:
            ys = 0
            new_habitat = input("Nouvel habitat: ")
            for a in animals:
                if a.id == mdf:
                    a.habitat = new_habitat
                    print("Animal modifie !")
                    ys += 1
            if ys == 0:
                print("Aucun animal trouve avec cet id !")
        elif choix == 2:
            ys = 0
            new_age = int(input("Nouveau animal : "))
            for a in animals:
                if a.id == mdf:
                    a.age = new_age
                    print("Animal modifie !")
                    ys += 1
            if ys == 0:
                print("Aucun animal trouve avec cet id !")
    elif choix == 4:
        ys = 0
        id_sup = int(input("Id de l'animal a supprimer: "))
        for a in animals:
            if a.id == id_sup:
                animals.remove(a)
                ys += 1
                print("Animal supprime!")
        if ys == 0:
                print("Aucun animal trouve avec cet id !")
    elif choix == 5:
        print("Rehercher un animal :")
        print("1. Par id")
        print("2. Par nom")
        print("3. Par especes")
        number = int(input("Choix >"))
        if number == 1:
            ys = 0
            id_rs = int(input("Id recherche: "))
            print(f"{'Id':<5}{'Nom':<10}{'Espece':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
            for a in animals:
                if a.id == id_rs:
                    ys += 1
                    print(f"{a.id:<5}{a.name:<10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
            if ys == 0:
                    print("Aucun animal trouve.")
        elif number == 2:
            ys = 0
            name_rs = input("Nom recherche: ")
            print(f"{'Id':<5}{'Nom':<10}{'Espece':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
            for a in animals:
                if a.name == name_rs:
                    ys += 1
                    print(f"{a.id:<5}{a.name:<10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
            if ys == 0:
                    print("Aucun animal trouve.")
        elif number == 3:
                    ys = 0
                    espece_rs = input("Nom recherche: ")
                    print(f"{'Id':<5}{'Nom':<10}{'Espece':<10}{'Age':<5}{'Habitat':<10}{'Poids':<5}")
                    for a in animals:
                        if a.species == espece_rs:
                            ys += 1
                            print(f"{a.id:<5}{a.name:<10}{a.species:<10}{a.age:<5}{a.habitat:<10}{a.poids:<5}")
                    if ys == 0:
                        print("Aucun animal trouve.")
    elif choix == 6:
        print("=== Statistique ===")
        print("Nombre total d'animaux: ",len(animals))
        total = 0
        for a in animals:
            total += a.age
        print("Age moyen:", round(total/len(animals),1))
        oldest = max(animals, key=lambda a: a.age)
        oldest_name = oldest.name
        youngest = min(animals, key=lambda a: a.age)
        youngest_name = youngest.name
        print("Animal le plus vieux: ",oldest_name," (",oldest.age," ans)",sep="")
        print("Animal le plus jeunes:",youngest_name," (",youngest.age," ans)",sep="")
        espece_count = {}
        for a in animals:
            if a.species in espece_count:
                espece_count[a.species] += 1
            else:
                espece_count[a.species] = 1
    elif choix == 0:
        print("Au revoir!")
        break
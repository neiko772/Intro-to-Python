# Functions with Parameters

astronaut_name = input("Welcome astronaut. What is your name?")
companion_name  = input("What is your companion's name? ")

def greet_astronaut(name):
    print(f"Hello, {name}! Welcome to the mission.")

    greet_astronaut(astronaut_name)

    greet_astronaut(companion_name)

    #! Multiple Parameters 
    def greet_all_astronauts(astronaut1, astronaut2):
        print(f"Hello, {astronaut1} and {astronaut2}! Welcome to the mission.")

        greet_all_astronauts(astronaut_name, companion_name)
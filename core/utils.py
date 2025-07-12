import random

nato = [
    "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel",
    "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
    "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
    "X-ray", "Yankee", "Zulu"
]

def generate_callsign():
    while True:
        c1, c2 = random.choice(nato) , random.randint(0,69)
        callsign = f"{c1}{c2}"
        return callsign

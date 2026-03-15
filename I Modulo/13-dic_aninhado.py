import pprint

games = {
    "Resident Evil 4": {
        "yearLaunch": 2005,
        "gamePrice": 150.00,
        "classification": 9.5,
        "genre": ["terror", "ação"]
    },
    "Fifa 23": {
        "yearLaunch": 2022,
        "gamePrice": 250.99,
        "classification": 7.9,
        "genre": ["esporte", "familia"]
    },
    "The Legend of Zelda": {
        "yearLaunch": 1986,
        "gamePrice": 300.00,
        "classification": 9.8,
        "genre": ["aventura", "ação"]
    },
    "Mario Odyssey": {
        "yearLaunch": 2017,
        "gamePrice": 200.00,
        "classification": 9.7,
        "genre": ["aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(games)
print(" ")
print(games["Mario Odyssey"]["yearLaunch"])
print(games["Fifa 23"]["genre"][0])

games["Resident Evil 4"]["genre"].append("survival horror")
pp.pprint(games)
print("-"*30)
del games["The Legend of Zelda"]
pp.pprint(games)
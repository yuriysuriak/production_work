from api.star_wars_api import StarWarsApi

def print_movie_info(movie_id):
    api_client = StarWarsApi()

    film = api_client.get_entity('films', movie_id)
    print(f"Фільм: {film['title']}")

    print("Персонажі:")
    characters = film['characters']
    for i, character_url in enumerate(characters, start=1):
        character_data = api_client.get_entity('people', character_url.split('/')[-2])
        homeworld_data = api_client.get_entity('planets', character_data['homeworld'].split('/')[-2])
        print(f" {i}. {character_data['name']} з планети {homeworld_data['name']}")

    print("Транспортні засоби:")
    vehicles = film['vehicles']
    for i, vehicle_url in enumerate(vehicles, start=1):
        vehicle_data = api_client.get_entity('vehicles', vehicle_url.split('/')[-2])
        print(f" {i}. {vehicle_data['name']}")

    print("Космічні кораблі:")
    starships = film['starships']
    for i, starship_url in enumerate(starships, start=1):
        starship_data = api_client.get_entity('starships', starship_url.split('/')[-2])
        print(f" {i}. {starship_data['name']}")

    print("Види істот:")
    species = film['species']
    for i, specie_url in enumerate(species, start=1):
        specie_data = api_client.get_entity('species', specie_url.split('/')[-2])
        print(f" {i}. {specie_data['name']}")

def main():
    movie_id = input("Введіть ID фільму: ")
    print_movie_info(movie_id)

if __name__ == "__main__":
    main()

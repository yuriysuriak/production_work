from api_star_wars import StarWarsApi

def print_movie_info(movie_id):
    api_client = StarWarsApi()

    film = api_client.get_entity('films', movie_id)
    print(f"Фільм: {film['title']}")

    print("Персонажі:")
    characters = film['characters']
    for character_url in characters:
        character_data = api_client.get_entity('people', character_url.split('/')[-2])
        homeworld_data = api_client.get_entity('planets', character_data['homeworld'].split('/')[-2])
        print(f" {character_data['name']} з планети {homeworld_data['name']}")

    print("Транспортні засоби:")
    vehicles = film['vehicles']
    for vehicle_url in vehicles:
        vehicle_data = api_client.get_entity('vehicles', vehicle_url.split('/')[-2])
        print(f" {vehicle_data['name']}")

    print("Космічні кораблі:")
    starships = film['starships']
    for starship_url in starships:
        starship_data = api_client.get_entity('starships', starship_url.split('/')[-2])
        print(f" {starship_data['name']}")

    print("Види істот:")
    species = film['species']
    for specie_url in species:
        specie_data = api_client.get_entity('species', specie_url.split('/')[-2])
        print(f" {specie_data['name']}")

def main():
    movie_id = input("Введіть ID фільму: ")
    print_movie_info(movie_id)

if __name__ == "__main__":
    main()

import requests


def pokemonbul():
    try:
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
        pokemon_response = requests.get(pokemon_url)

        status_code= pokemon_response.status_code

        max_id_count="#1281"

        giris = input("Bir Pokemon ismi ya da ID'si giriniz:")
        girdi = giris
        id_or_name = girdi.lower()
        payload = f"{id_or_name}/"
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{payload}"
        pokemon_response = requests.get(pokemon_url)
        data = pokemon_response.json()




        if status_code == 200:
            pokemon_id = data["id"]
            pokemon_name = data["name"]
            pokemon_type1 = data["types"][0]["type"]["name"]
            pokemon_height=data["height"]/10
            pokemon_weight=data["weight"]/10
            if len(data["types"]) == 1:

                print(f"id:\t#{pokemon_id:}\n"
                      f"isim:\t{pokemon_name}\n"
                      f"tür:\t{pokemon_type1}\n"
                      f"uzunluk:\t{pokemon_height} metre\n"
                      f"ağırlık:\t{pokemon_weight} kilo")

            elif len(data["types"]) > 1:
                pokemon_type2 = data["types"][1]["type"]["name"]

                print(f"id:\t#{pokemon_id}\n"
                      f"isim:\t{pokemon_name}\n"
                      f"tür:\t{pokemon_type1}/{pokemon_type2}\n"
                      f"uzunluk:\t{pokemon_height}\n"
                      f"ağırlık:\t{pokemon_weight}")
        else:
            print("server'a bağlanılamıyor...")
            
    except:
        print(f"Hatalı bir index numarası ya da pokemon ismi girdiniz. Tekrar deneyin (max pokemon index:\t{max_id_count}) ")

pokemonbul()



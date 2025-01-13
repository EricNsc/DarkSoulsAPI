from fastapi import FastAPI, HTTPException
import json

app = FastAPI()



@app.get("/weapons/names")
async def get_weapon_names():
    
    with open('DarkSoulsWeapons.json', 'r') as file:
        weapons_data = json.load(file)

    
    weapon_names = [weapon['name'] for weapon in weapons_data]

    return weapon_names


@app.get("/{weapon}")
async def get_weapon_details(weapon: str):
    
    with open('DarkSoulsWeapons.json', 'r') as file:
        weapons_data = json.load(file)

    
    weapon_data = next((w for w in weapons_data if w['name'].lower() == weapon.lower()), None)

    if weapon_data is None:
        raise HTTPException(status_code=404, detail=f"Weapon '{weapon}' not found.")

    return weapon_data


@app.get("/{weapon}/attributes={attributes}")
async def get_weapon_attributes(weapon: str, attributes: str):
    # Carregar os dados do arquivo JSON
    with open('DarkSoulsWeapons.json', 'r') as file:
        weapons_data = json.load(file)

    
    weapon_data = next((w for w in weapons_data if w['name'].lower() == weapon.lower()), None)

    if weapon_data is None:
        raise HTTPException(status_code=404, detail=f"Weapon '{weapon}' not found.")

    
    attributes_list = attributes.split('&')  

    if len(attributes_list) == 1:  
        keys = attributes_list[0].split('.')  
        data = weapon_data

        try:
            for key in keys:  
                data = data[key]
            return data  
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Attribute '{attributes_list[0]}' not found.")

    
    result = {}
    for attr in attributes_list:
        keys = attr.split('.')
        data = weapon_data

        try:
            for key in keys:
                data = data[key]
            result[attr] = data
        except KeyError:
            result[attr] = "Attribute not found"

    return result

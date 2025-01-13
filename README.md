# DarkSoulsAPI
API that provides detailed statistics for weapons in Dark Souls
<br>
<br>
<br>

## how to make it run: 

1. git clone https://github.com/EricNsc/DarkSoulsAPI<br><br>
2. requirements: <br> **fastapi** <br> **uvicorn**<br><br>
3. run: `python -m uvicorn main:app --reload`
<br>

## Endpoints:
`/weapon/names`
Retrieve names for all the weapons.
<br>
<br>

`/{weapon}`
Retrieve all details for the specified weapon.<br>
`GET /Greatsword%20of%20Artorias`
<br>
<br>

`/{weapon}/attributes={attribute}`
Retrieve a specific attribute of a weapon.<br>
`GET /Greatsword%20of%20Artorias/attributes=atk` Retrieves all attack types (physical, magic, fire, etc.)<br>
`GET /Greatsword%20of%20Artorias/attributes=atk&scale` Retrieves both attack and scaling information.
<br>
<br>

**You can specify the type of attribute using {attribute}.{type}.**<br>
Example:<br>
`GET /Greatsword%20of%20Artorias/attributes=atk.physical`
Retrieves only the physical damage.<br>
`GET /Greatsword%20of%20Artorias/attributes=scale.faith`
Retrieves the faith scaling.
<br>
<br>



Supported Attributes:<br>
`atk`: All attack types (physical, magic, fire, lightning, bonus)<br>
`scale`: Scaling of the weapon (based on stats like strength, dexterity, intelligence, etc.)<br>
`weight`: Weight of the weapon<br>
`req`: Requirements<br>
`def`: Defenses<br>
`effects`: Effects dealt by the weapon<br>
`durability`: Durability of the weapon<br>
<br>
<br>


## For more advanced queries, you can combine multiple attributes separated by &:

Example:
`GET /Greatsword%20of%20Artorias/attributes=atk.physical&atk.magic&scale`

This will retrieve physical and magic attack values along with scaling information.
<br>
<br>

> [!NOTE]
>All weapon names must be URL-encoded (e.g., spaces as %20).<br>
>The API currently works only locally.

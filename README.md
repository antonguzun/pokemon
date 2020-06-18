## Deploy
copy .env_example to .env

build and run
```shell script
sudo docker-compose build
sudo docker-compose up
```

## API examples
you can filter by name or rages of attack, defense or hp
```http request
http://0.0.0.0:8010/pokemon/?format=json;attack_from=35;attack_to=50;page=1

http://0.0.0.0:8010/pokemon/?format=json;hp_from=35;hp_to=92;page=2

http://0.0.0.0:8010/pokemon/?format=json;hp_from=35;hp_to=92;page=10

http://0.0.0.0:8010/pokemon/?format=json;name=Bulbasaur

http://0.0.0.0:8010/pokemon/?format=json;name=Bulbas

http://0.0.0.0:8010/pokemon/?format=json;name=Bulbas;hp_from=40;hp_to=50

```
## JSON response examples
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Bulbasaur",
      "type_1": {
        "type_name": "Grass"
      },
      "type_2": {
        "type_name": "Poison"
      },
      "total": 318,
      "hp": 45,
      "attack": 49,
      "defense": 49,
      "spell_attack": 65,
      "spell_defense": 65,
      "speed": 45,
      "generation": 1
    }
  ]
}
```
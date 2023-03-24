class Pokémon():
        def __init__(self,Level=5,Name='Pokémon',Type='normal'):
                self.name=Name
                self.level=Level
                self.type=Type
                self.max_health=self.level*5
                self.health=self.level*5
                self.this_pokemon_excists=True
                while self.this_pokemon_excists:
                        if self.health==0:
                                self.knock_out()
                self.is_knocked_out=False
        def lose_health(self):
                if current_health < 0:
                        self.knock_out()
                elif current_health>0:
                        self.health-=1
                else:
                        self.knock_out()
                return self.name+' lost 1 health, health now '+self.health
        def knock_out(self,winner):
                self.is_knocked_out=True
                return self.name+' was knocked out of battle from '+ winner.name
        def regain_health(self,trainer):
                trainer.number_of_potions-=1
                if self.health==self.max_health:
                        print('Already max health')
                        self.lose_health()
                else:
                     self.health+=1
                return f'Health now {self.health}'
        def attack(self,other_pokemon):
                other_pokemon.lose_health()
                return other_pokemon.name+' was attacked by '+self.name
class Trainer:
        def __init__(self,pokemon,name,potions,active_pokemon):
                self.all_pokemon=pokemon
                self.name=name
                self.number_of_potions=potions
                self.currently_active_pokemon=active_pokemon
        def use_potion(self,pokekmon_to_heal):
                pokemon_to_heal.regain_health()

Test_Pikachu=Pokémon(Name='Pikachu', Type='Electric')

import random
class Soldier():
    def __init__(self,id,team):
        self.id=id
        self.team=team

    def follow_hero(self,hero):
        print(f"Воин #{self.id} следует за героем #{hero.id}")

class Hero():
    def __init__(self,id,team):
        self.id=id
        self.team=team
        self.level=1

    def increase_level(self):
        self.level+=1

team1=[]
team2=[]

hero1=Hero(1,'Команда 1')
hero2=Hero(2,'Команда 2')

for i in range (1000):
    team=random.choice(['Команда 1','Команда 2'])
    soldier=Soldier(i,team)
    if team=='Команда 1':
        team1.append(soldier)
    else:
        team2.append(soldier)

print(f"Количество солдат героя #1:{len(team1)}")
print(f"Количество солдат героя #2:{len(team2)}")

if len(team1)>len(team2):
    print("Уровень героя #1 повышен")
else:
    print("Уровень героя #2 повышен")

follow=random.choice(team1)
follow.follow_hero(hero1)
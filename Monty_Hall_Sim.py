import matplotlib.pyplot as plt
class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def show_suit(self):
        return self.suit


    def __repr__(self):
        return f"{self.rank} of {self.suit}"

deck=[card(1, 'heart'), card(2, 'heart'), card(3, 'spade')]

def algorithm_switch(deck):
    import random
    shuffled_deck=shuffler(deck)
    return game(shuffled_deck, random.randint(0, 2), 'y')


def shuffler(deck):
    import random
    random.shuffle(deck)
    return deck

def game(deck,number,switch):
   
    shuffled_deck=shuffler(deck)
    choose=number
    for index in range(len(deck)):
        if index != choose:
            if deck[index].show_suit() == 'heart':
                
                choice=switch
                if choice == 'y':
                    for i in range(len(deck)):
                        if i != index and i != choose:
                                if deck[i].show_suit() == 'spade':
                                    return 1
                                else:
                                    return 0
                else:
                    if deck[choose].show_suit() == 'spade':
                        return 1
                    else:
                        return 0
                break
                            
print(deck)
shuffled_deck=shuffler(deck)
for index in range(len(shuffled_deck)):
    print(shuffled_deck[index].show_suit(),end=' ')
import random
print( game(shuffled_deck, random.randint(0, 2), 'y') )

def simulator(trials):
    switch_wins=0
    stay_wins=0
    for i in range(trials):
        if game(deck, random.randint(0, 2), 'y') == 1:
            switch_wins+=1
        if game(deck, random.randint(0, 2), 'n') == 1:
            stay_wins+=1
    print(f"Switch win percentage: {switch_wins/trials*100}%")
    print(f"Stay win percentage: {stay_wins/trials*100}%")

simulator(10000)

def one_strategy(trials):
    total_switch_game=int(2/3*trials)
    total_stay_game=int(1/3*trials)
    switch_wins=0
    stay_wins=0
    for i in range(total_switch_game):
        if game(deck, random.randint(0, 2), 'y') == 1:
            switch_wins+=1
    for i in range(total_stay_game):
        if game(deck, random.randint(0, 2), 'n') == 1:
            stay_wins+=1
    print(f"Switch win percentage: {switch_wins/total_switch_game*100}%")
    print(f"Stay win percentage: {stay_wins/total_stay_game*100}%")
    print(f"Overall win percentage: {(switch_wins+stay_wins)/trials*100}%")
one_strategy(10000)

def plot_simulation(trials):
    switch_wins = 0
    stay_wins = 0
    switch_percentages = []
    stay_percentages = []
    for i in range(1, trials + 1):
        if game(deck, random.randint(0, 2), 'y'):
            switch_wins += 1
        if game(deck, random.randint(0, 2), 'n'):
            stay_wins += 1
        switch_percentages.append(switch_wins / i)
        stay_percentages.append(stay_wins / i)
    
    # Plot
    plt.plot(range(1, trials + 1), switch_percentages, label='Switch Win %')
    plt.plot(range(1, trials + 1), stay_percentages, label='Stay Win %')
    plt.axhline(2/3, color='blue', linestyle='--', alpha=0.5)
    plt.axhline(1/3, color='orange', linestyle='--', alpha=0.5)
    plt.xlabel('Number of Trials')
    plt.ylabel('Cumulative Win Percentage')
    plt.title('Monty Hall Simulation: Switch vs Stay')
    plt.legend()
    plt.show()

plot_simulation(10000)

import csv
import matplotlib.pyplot as plt

# Reads Data
def read_csv(filename):
    champions_data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            champions_data.append(row)
    return champions_data

def plot_champion_stats(champions_data):
    champions = [champion['Champion'] for champion in champions_data]
    kills = [int(champion['Kills']) for champion in champions_data]
    deaths = [int(champion['Deaths']) for champion in champions_data]
    assists = [int(champion['Assists']) for champion in champions_data]
    games_played = [int(champion['Games Played']) for champion in champions_data]
    total_damage = [int(champion['Total Damage Dealt']) for champion in champions_data]
    games_won = [int(champion['Games Won']) for champion in champions_data]
    games_lost = [int(champion['Games Lost']) for champion in champions_data]

    x = range(len(champions))

    # Create subplots for each stat
    fig, ax = plt.subplots(4, 2, figsize=(14, 14))

    # Kills
    ax[0, 0].bar(x, kills, color='green')
    ax[0, 0].set_title('Kills by Champion')
    ax[0, 0].set_xticks(x)
    ax[0, 0].set_xticklabels(champions, rotation=45)
    ax[0, 0].set_ylabel('Kills')

    # Deaths
    ax[0, 1].bar(x, deaths, color='red')
    ax[0, 1].set_title('Deaths by Champion')
    ax[0, 1].set_xticks(x)
    ax[0, 1].set_xticklabels(champions, rotation=45)
    ax[0, 1].set_ylabel('Deaths')

    # Assists
    ax[1, 0].bar(x, assists, color='blue')
    ax[1, 0].set_title('Assists by Champion')
    ax[1, 0].set_xticks(x)
    ax[1, 0].set_xticklabels(champions, rotation=45)
    ax[1, 0].set_ylabel('Assists')

    # Games Played
    ax[1, 1].bar(x, games_played, color='purple')
    ax[1, 1].set_title('Games Played by Champion')
    ax[1, 1].set_xticks(x)
    ax[1, 1].set_xticklabels(champions, rotation=45)
    ax[1, 1].set_ylabel('Games Played')

    # Total Damage Dealt
    ax[2, 0].bar(x, total_damage, color='orange')
    ax[2, 0].set_title('Total Damage Dealt by Champion')
    ax[2, 0].set_xticks(x)
    ax[2, 0].set_xticklabels(champions, rotation=45)
    ax[2, 0].set_ylabel('Total Damage Dealt')

    # Games Won
    ax[2, 1].bar(x, games_won, color='cyan')
    ax[2, 1].set_title('Games Won by Champion')
    ax[2, 1].set_xticks(x)
    ax[2, 1].set_xticklabels(champions, rotation=45)
    ax[2, 1].set_ylabel('Games Won')

    # Games Lost
    ax[3, 0].bar(x, games_lost, color='magenta')
    ax[3, 0].set_title('Games Lost by Champion')
    ax[3, 0].set_xticks(x)
    ax[3, 0].set_xticklabels(champions, rotation=45)
    ax[3, 0].set_ylabel('Games Lost')

    # Hide the empty subplot in the last row and last column
    ax[3, 1].axis('off')

    # Adjust layout
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    filename = 'data/cleaned_data.csv'
    champions_data = read_csv(filename)
    plot_champion_stats(champions_data)

import csv
from collections import defaultdict

def clean_data(csv_filename='data/data.csv', output_filename='data/cleaned_data.csv'):
    # Initialize a dictionary to hold data
    cleaned_data = defaultdict(lambda: {
        'Kills': 0,
        'Deaths': 0,
        'Assists': 0,
        'Gold Earned': 0,
        'Damage Dealt to Objectives': 0,
        'Total Damage Dealt': 0,
        'Total Damage Dealt to Champions': 0,
        'Total Damage Taken': 0,
        'Total Minions Killed': 0,
        'Physical Damage Dealt': 0,
        'Magic Damage Dealt': 0,
        'Games Played': 0,
        'Games Won': 0,
        'Games Lost': 0
    })

    # Read data from the CSV file
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            champion = row['Champion']
            cleaned_data[champion]['Kills'] += int(row['Kills'])
            cleaned_data[champion]['Deaths'] += int(row['Deaths'])
            cleaned_data[champion]['Assists'] += int(row['Assists'])
            cleaned_data[champion]['Gold Earned'] += int(row['Gold Earned'])
            cleaned_data[champion]['Damage Dealt to Objectives'] += int(row['Damage Dealt to Objectives'])
            cleaned_data[champion]['Total Damage Dealt'] += int(row['Total Damage Dealt'])
            cleaned_data[champion]['Total Damage Dealt to Champions'] += int(row['Total Damage Dealt to Champions'])
            cleaned_data[champion]['Total Damage Taken'] += int(row['Total Damage Taken'])
            cleaned_data[champion]['Total Minions Killed'] += int(row['Total Minions Killed'])
            cleaned_data[champion]['Physical Damage Dealt'] += int(row['Physical Damage Dealt'])
            cleaned_data[champion]['Magic Damage Dealt'] += int(row['Magic Damage Dealt'])
            cleaned_data[champion]['Games Played'] += 1

            # Increment games won or lost based on the 'Win' value
            if row['Win'] == 'True':
                cleaned_data[champion]['Games Won'] += 1
            else:
                cleaned_data[champion]['Games Lost'] += 1

    # Write clean data to a new CSV file
    with open(output_filename, mode='w', newline='') as file:
        fieldnames = ['Champion', 'Kills', 'Deaths', 'Assists', 'Gold Earned',
                      'Damage Dealt to Objectives', 'Total Damage Dealt',
                      'Total Damage Dealt to Champions', 'Total Damage Taken',
                      'Total Minions Killed', 'Physical Damage Dealt',
                      'Magic Damage Dealt', 'Games Played', 'Games Won', 'Games Lost']
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for champion, data in cleaned_data.items():
            data['Champion'] = champion
            writer.writerow(data)

if __name__ == '__main__':
    clean_data()

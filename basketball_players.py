'''
The goal of this project is to read all the tables in https://www.basketball-reference.com/players
and store the information about all the players in a single csv file
'''
import pandas
import os
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in letters:
    players_df = pandas.read_html(f'https://www.basketball-reference.com/players/{i}/')[0]
    players_df.to_csv(f'{i.upper()}_players.csv')
'''lines 4,5, and 6 make use of a for loop to iterate over each page,
convert the table in each page to a pandas dataframe and store each of them in
a separate csv file. example, the players with names starting with the leter A are 
stored in a csv file named A_players.csv
those whose names start with the letter B are stored in a csv file named 
B_players.csv similarly, C_players.csv, D_players.csv, etc
'''

player_csv = [file for file in os.listdir() if file.endswith('.csv')]
#Stores all the csv files(A_players.csv, Bplayers.csv, C_players.csv, etc) in a list


df = pandas.concat(map(pandas.read_csv,player_csv),ignore_index=True)
#Reads all the csv_files in the list


df.to_csv('BasketBallPlayers.csv')
#Combines all the csv files to a single csv file called BasketBallPlayers.csv


'''
Since our goal is to join them all in a single csv file,we delete all the individual
csv files(A_players.csv,B_players.csv,C_players.csv, etc)
So that we have only one single csv file(BasketBallPlayers.csv) containing all the players from A-Z
'''
for file in os.listdir():
    if file.endswith('_players.csv'):
        os.remove(file)
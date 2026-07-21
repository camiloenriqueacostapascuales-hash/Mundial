from flask import Flask, render_template

app = Flask(__name__)

# World Cup History (1930 - 2026)
history_data = [
    {"year": "1930", "host": "Uruguay", "champion": "Uruguay", "runner_up": "Argentina", "teams": 13, "goals": 70, "top_scorer": "Guillermo Stábile (8)"},
    {"year": "1934", "host": "Italia", "champion": "Italia", "runner_up": "Checoslovaquia", "teams": 16, "goals": 70, "top_scorer": "Oldřich Nejedlý (5)"},
    {"year": "1938", "host": "Francia", "champion": "Italia", "runner_up": "Hungría", "teams": 15, "goals": 84, "top_scorer": "Leônidas (7)"},
    {"year": "1950", "host": "Brasil", "champion": "Uruguay", "runner_up": "Brasil", "teams": 13, "goals": 88, "top_scorer": "Ademir (8)"},
    {"year": "1954", "host": "Suiza", "champion": "Alemania Federal", "runner_up": "Hungría", "teams": 16, "goals": 140, "top_scorer": "Sándor Kocsis (11)"},
    {"year": "1958", "host": "Suecia", "champion": "Brasil", "runner_up": "Suecia", "teams": 16, "goals": 126, "top_scorer": "Just Fontaine (13)"},
    {"year": "1962", "host": "Chile", "champion": "Brasil", "runner_up": "Checoslovaquia", "teams": 16, "goals": 89, "top_scorer": "Garrincha et al. (4)"},
    {"year": "1966", "host": "Inglaterra", "champion": "Inglaterra", "runner_up": "Alemania Federal", "teams": 16, "goals": 89, "top_scorer": "Eusébio (9)"},
    {"year": "1970", "host": "México", "champion": "Brasil", "runner_up": "Italia", "teams": 16, "goals": 95, "top_scorer": "Gerd Müller (10)"},
    {"year": "1974", "host": "Alemania Federal", "champion": "Alemania Federal", "runner_up": "Países Bajos", "teams": 16, "goals": 97, "top_scorer": "Grzegorz Lato (7)"},
    {"year": "1978", "host": "Argentina", "champion": "Argentina", "runner_up": "Países Bajos", "teams": 16, "goals": 102, "top_scorer": "Mario Kempes (6)"},
    {"year": "1982", "host": "España", "champion": "Italia", "runner_up": "Alemania Federal", "teams": 24, "goals": 146, "top_scorer": "Paolo Rossi (6)"},
    {"year": "1986", "host": "México", "champion": "Argentina", "runner_up": "Alemania Federal", "teams": 24, "goals": 132, "top_scorer": "Gary Lineker (6)"},
    {"year": "1990", "host": "Italia", "champion": "Alemania Federal", "runner_up": "Argentina", "teams": 24, "goals": 115, "top_scorer": "Salvatore Schillaci (6)"},
    {"year": "1994", "host": "Estados Unidos", "champion": "Brasil", "runner_up": "Italia", "teams": 24, "goals": 141, "top_scorer": "Stoichkov, Salenko (6)"},
    {"year": "1998", "host": "Francia", "champion": "Francia", "runner_up": "Brasil", "teams": 32, "goals": 171, "top_scorer": "Davor Šuker (6)"},
    {"year": "2002", "host": "Corea/Japón", "champion": "Brasil", "runner_up": "Alemania", "teams": 32, "goals": 161, "top_scorer": "Ronaldo (8)"},
    {"year": "2006", "host": "Alemania", "champion": "Italia", "runner_up": "Francia", "teams": 32, "goals": 147, "top_scorer": "Miroslav Klose (5)"},
    {"year": "2010", "host": "Sudáfrica", "champion": "España", "runner_up": "Países Bajos", "teams": 32, "goals": 145, "top_scorer": "Müller, Villa, Sneijder, Forlán (5)"},
    {"year": "2014", "host": "Brasil", "champion": "Alemania", "runner_up": "Argentina", "teams": 32, "goals": 171, "top_scorer": "James Rodríguez (6)"},
    {"year": "2018", "host": "Rusia", "champion": "Francia", "runner_up": "Croacia", "teams": 32, "goals": 169, "top_scorer": "Harry Kane (6)"},
    {"year": "2022", "host": "Catar", "champion": "Argentina", "runner_up": "Francia", "teams": 32, "goals": 172, "top_scorer": "Kylian Mbappé (8)"},
    {"year": "2026", "host": "EE. UU. / México / Canadá", "champion": "Por definir", "runner_up": "Por definir", "teams": 48, "goals": "-", "top_scorer": "-", "upcoming": True}
]

# 48 Teams for 2026
teams_data = [
    # CONMEBOL
    {"name": "Argentina", "flag": "🇦🇷", "confed": "CONMEBOL", "players": [
        {"name": "Emiliano Martínez", "number": 23, "club": "Aston Villa", "position": "POR"},
        {"name": "Cristian Romero", "number": 13, "club": "Tottenham", "position": "DEF"},
        {"name": "Enzo Fernández", "number": 8, "club": "Chelsea", "position": "MED"},
        {"name": "Lionel Messi", "number": 10, "club": "Inter Miami", "position": "DEL"},
        {"name": "Julián Álvarez", "number": 9, "club": "Man City", "position": "DEL"}
    ]},
    {"name": "Brasil", "flag": "🇧🇷", "confed": "CONMEBOL", "players": [
        {"name": "Alisson", "number": 1, "club": "Liverpool", "position": "POR"},
        {"name": "Marquinhos", "number": 4, "club": "PSG", "position": "DEF"},
        {"name": "Bruno Guimarães", "number": 8, "club": "Newcastle", "position": "MED"},
        {"name": "Vinícius Júnior", "number": 7, "club": "Real Madrid", "position": "DEL"},
        {"name": "Rodrygo", "number": 10, "club": "Real Madrid", "position": "DEL"}
    ]},
    {"name": "Colombia", "flag": "🇨🇴", "confed": "CONMEBOL", "players": [
        {"name": "Camilo Vargas", "number": 12, "club": "Atlas", "position": "POR"},
        {"name": "Carlos Cuesta", "number": 2, "club": "Genk", "position": "DEF"},
        {"name": "Richard Ríos", "number": 6, "club": "Palmeiras", "position": "MED"},
        {"name": "James Rodríguez", "number": 10, "club": "São Paulo", "position": "MED"},
        {"name": "Luis Díaz", "number": 7, "club": "Liverpool", "position": "DEL"}
    ]},
    {"name": "Ecuador", "flag": "🇪🇨", "confed": "CONMEBOL", "players": [
        {"name": "Alexander Domínguez", "number": 22, "club": "LDU", "position": "POR"},
        {"name": "Piero Hincapié", "number": 3, "club": "Bayer Leverkusen", "position": "DEF"},
        {"name": "Moisés Caicedo", "number": 23, "club": "Chelsea", "position": "MED"},
        {"name": "Kendry Páez", "number": 10, "club": "Independiente del Valle", "position": "MED"},
        {"name": "Enner Valencia", "number": 13, "club": "Internacional", "position": "DEL"}
    ]},
    {"name": "Uruguay", "flag": "🇺🇾", "confed": "CONMEBOL", "players": [
        {"name": "Sergio Rochet", "number": 1, "club": "Internacional", "position": "POR"},
        {"name": "Ronald Araújo", "number": 4, "club": "Barcelona", "position": "DEF"},
        {"name": "Federico Valverde", "number": 15, "club": "Real Madrid", "position": "MED"},
        {"name": "Nicolás de la Cruz", "number": 7, "club": "Flamengo", "position": "MED"},
        {"name": "Darwin Núñez", "number": 9, "club": "Liverpool", "position": "DEL"}
    ]},
    {"name": "Paraguay", "flag": "🇵🇾", "confed": "CONMEBOL", "players": [
        {"name": "Carlos Coronel", "number": 1, "club": "NY Red Bulls", "position": "POR"},
        {"name": "Gustavo Gómez", "number": 15, "club": "Palmeiras", "position": "DEF"},
        {"name": "Mathías Villasanti", "number": 23, "club": "Gremio", "position": "MED"},
        {"name": "Miguel Almirón", "number": 10, "club": "Newcastle", "position": "MED"},
        {"name": "Julio Enciso", "number": 19, "club": "Brighton", "position": "DEL"}
    ]},
    {"name": "Venezuela", "flag": "🇻🇪", "confed": "CONMEBOL", "players": [
        {"name": "Rafael Romo", "number": 22, "club": "U. Católica", "position": "POR"},
        {"name": "Yordan Osorio", "number": 3, "club": "Parma", "position": "DEF"},
        {"name": "Yangel Herrera", "number": 6, "club": "Girona", "position": "MED"},
        {"name": "Yeferson Soteldo", "number": 10, "club": "Gremio", "position": "MED"},
        {"name": "Salomón Rondón", "number": 23, "club": "Pachuca", "position": "DEL"}
    ]},
    
    # UEFA
    {"name": "Francia", "flag": "🇫🇷", "confed": "UEFA", "players": [
        {"name": "Mike Maignan", "number": 16, "club": "AC Milan", "position": "POR"},
        {"name": "William Saliba", "number": 2, "club": "Arsenal", "position": "DEF"},
        {"name": "Aurélien Tchouaméni", "number": 8, "club": "Real Madrid", "position": "MED"},
        {"name": "Antoine Griezmann", "number": 7, "club": "Atlético Madrid", "position": "DEL"},
        {"name": "Kylian Mbappé", "number": 10, "club": "Real Madrid", "position": "DEL"}
    ]},
    {"name": "España", "flag": "🇪🇸", "confed": "UEFA", "players": [
        {"name": "Unai Simón", "number": 23, "club": "Athletic Club", "position": "POR"},
        {"name": "Aymeric Laporte", "number": 14, "club": "Al-Nassr", "position": "DEF"},
        {"name": "Rodri", "number": 16, "club": "Man City", "position": "MED"},
        {"name": "Lamine Yamal", "number": 19, "club": "Barcelona", "position": "DEL"},
        {"name": "Álvaro Morata", "number": 7, "club": "Atlético Madrid", "position": "DEL"}
    ]},
    {"name": "Alemania", "flag": "🇩🇪", "confed": "UEFA", "players": [
        {"name": "Marc-André ter Stegen", "number": 1, "club": "Barcelona", "position": "POR"},
        {"name": "Antonio Rüdiger", "number": 2, "club": "Real Madrid", "position": "DEF"},
        {"name": "Florian Wirtz", "number": 17, "club": "Bayer Leverkusen", "position": "MED"},
        {"name": "Jamal Musiala", "number": 10, "club": "Bayern Munich", "position": "MED"},
        {"name": "Kai Havertz", "number": 7, "club": "Arsenal", "position": "DEL"}
    ]},
    {"name": "Portugal", "flag": "🇵🇹", "confed": "UEFA", "players": [
        {"name": "Diogo Costa", "number": 22, "club": "Porto", "position": "POR"},
        {"name": "Rúben Dias", "number": 4, "club": "Man City", "position": "DEF"},
        {"name": "Bruno Fernandes", "number": 8, "club": "Man United", "position": "MED"},
        {"name": "Bernardo Silva", "number": 10, "club": "Man City", "position": "MED"},
        {"name": "Rafael Leão", "number": 17, "club": "AC Milan", "position": "DEL"}
    ]},
    {"name": "Inglaterra", "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "confed": "UEFA", "players": [
        {"name": "Jordan Pickford", "number": 1, "club": "Everton", "position": "POR"},
        {"name": "John Stones", "number": 5, "club": "Man City", "position": "DEF"},
        {"name": "Jude Bellingham", "number": 10, "club": "Real Madrid", "position": "MED"},
        {"name": "Phil Foden", "number": 11, "club": "Man City", "position": "MED"},
        {"name": "Harry Kane", "number": 9, "club": "Bayern Munich", "position": "DEL"}
    ]},
    {"name": "Países Bajos", "flag": "🇳🇱", "confed": "UEFA", "players": [
        {"name": "Bart Verbruggen", "number": 1, "club": "Brighton", "position": "POR"},
        {"name": "Virgil van Dijk", "number": 4, "club": "Liverpool", "position": "DEF"},
        {"name": "Frenkie de Jong", "number": 21, "club": "Barcelona", "position": "MED"},
        {"name": "Xavi Simons", "number": 7, "club": "RB Leipzig", "position": "MED"},
        {"name": "Cody Gakpo", "number": 11, "club": "Liverpool", "position": "DEL"}
    ]},
    {"name": "Italia", "flag": "🇮🇹", "confed": "UEFA", "players": [
        {"name": "Gianluigi Donnarumma", "number": 1, "club": "PSG", "position": "POR"},
        {"name": "Alessandro Bastoni", "number": 21, "club": "Inter", "position": "DEF"},
        {"name": "Nicolò Barella", "number": 18, "club": "Inter", "position": "MED"},
        {"name": "Federico Chiesa", "number": 14, "club": "Juventus", "position": "DEL"},
        {"name": "Gianluca Scamacca", "number": 9, "club": "Atalanta", "position": "DEL"}
    ]},
    {"name": "Bélgica", "flag": "🇧🇪", "confed": "UEFA", "players": [
        {"name": "Koen Casteels", "number": 1, "club": "Wolfsburg", "position": "POR"},
        {"name": "Wout Faes", "number": 4, "club": "Leicester City", "position": "DEF"},
        {"name": "Amadou Onana", "number": 24, "club": "Everton", "position": "MED"},
        {"name": "Kevin De Bruyne", "number": 7, "club": "Man City", "position": "MED"},
        {"name": "Romelu Lukaku", "number": 10, "club": "Roma", "position": "DEL"}
    ]},
    {"name": "Suiza", "flag": "🇨🇭", "confed": "UEFA", "players": [
        {"name": "Yann Sommer", "number": 1, "club": "Inter", "position": "POR"},
        {"name": "Manuel Akanji", "number": 5, "club": "Man City", "position": "DEF"},
        {"name": "Granit Xhaka", "number": 10, "club": "Bayer Leverkusen", "position": "MED"},
        {"name": "Xherdan Shaqiri", "number": 23, "club": "Chicago Fire", "position": "MED"},
        {"name": "Breel Embolo", "number": 7, "club": "Monaco", "position": "DEL"}
    ]},
    {"name": "Croacia", "flag": "🇭🇷", "confed": "UEFA", "players": [
        {"name": "Dominik Livaković", "number": 1, "club": "Fenerbahçe", "position": "POR"},
        {"name": "Joško Gvardiol", "number": 4, "club": "Man City", "position": "DEF"},
        {"name": "Mateo Kovačić", "number": 8, "club": "Man City", "position": "MED"},
        {"name": "Luka Modrić", "number": 10, "club": "Real Madrid", "position": "MED"},
        {"name": "Andrej Kramarić", "number": 9, "club": "Hoffenheim", "position": "DEL"}
    ]},
    {"name": "Dinamarca", "flag": "🇩🇰", "confed": "UEFA", "players": [
        {"name": "Kasper Schmeichel", "number": 1, "club": "Anderlecht", "position": "POR"},
        {"name": "Andreas Christensen", "number": 6, "club": "Barcelona", "position": "DEF"},
        {"name": "Pierre-Emile Højbjerg", "number": 23, "club": "Tottenham", "position": "MED"},
        {"name": "Christian Eriksen", "number": 10, "club": "Man United", "position": "MED"},
        {"name": "Rasmus Højlund", "number": 9, "club": "Man United", "position": "DEL"}
    ]},
    {"name": "Austria", "flag": "🇦🇹", "confed": "UEFA", "players": [
        {"name": "Patrick Pentz", "number": 1, "club": "Brøndby", "position": "POR"},
        {"name": "David Alaba", "number": 8, "club": "Real Madrid", "position": "DEF"},
        {"name": "Konrad Laimer", "number": 20, "club": "Bayern Munich", "position": "MED"},
        {"name": "Marcel Sabitzer", "number": 9, "club": "Dortmund", "position": "MED"},
        {"name": "Marko Arnautović", "number": 7, "club": "Inter", "position": "DEL"}
    ]},
    {"name": "Serbia", "flag": "🇷🇸", "confed": "UEFA", "players": [
        {"name": "Vanja Milinković-Savić", "number": 23, "club": "Torino", "position": "POR"},
        {"name": "Nikola Milenković", "number": 4, "club": "Fiorentina", "position": "DEF"},
        {"name": "Sergej Milinković-Savić", "number": 20, "club": "Al-Hilal", "position": "MED"},
        {"name": "Dušan Tadić", "number": 10, "club": "Fenerbahçe", "position": "MED"},
        {"name": "Aleksandar Mitrović", "number": 9, "club": "Al-Hilal", "position": "DEL"}
    ]},
    {"name": "Escocia", "flag": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "confed": "UEFA", "players": [
        {"name": "Angus Gunn", "number": 1, "club": "Norwich City", "position": "POR"},
        {"name": "Kieran Tierney", "number": 6, "club": "Real Sociedad", "position": "DEF"},
        {"name": "Scott McTominay", "number": 4, "club": "Man United", "position": "MED"},
        {"name": "John McGinn", "number": 7, "club": "Aston Villa", "position": "MED"},
        {"name": "Che Adams", "number": 10, "club": "Southampton", "position": "DEL"}
    ]},
    {"name": "Turquía", "flag": "🇹🇷", "confed": "UEFA", "players": [
        {"name": "Uğurcan Çakır", "number": 1, "club": "Trabzonspor", "position": "POR"},
        {"name": "Merih Demiral", "number": 3, "club": "Al-Ahli", "position": "DEF"},
        {"name": "Hakan Çalhanoğlu", "number": 10, "club": "Inter", "position": "MED"},
        {"name": "Arda Güler", "number": 8, "club": "Real Madrid", "position": "MED"},
        {"name": "Barış Alper Yılmaz", "number": 21, "club": "Galatasaray", "position": "DEL"}
    ]},
    {"name": "Ucrania", "flag": "🇺🇦", "confed": "UEFA", "players": [
        {"name": "Andriy Lunin", "number": 1, "club": "Real Madrid", "position": "POR"},
        {"name": "Illya Zabarnyi", "number": 13, "club": "Bournemouth", "position": "DEF"},
        {"name": "Oleksandr Zinchenko", "number": 17, "club": "Arsenal", "position": "MED"},
        {"name": "Mykhailo Mudryk", "number": 10, "club": "Chelsea", "position": "MED"},
        {"name": "Artem Dovbyk", "number": 11, "club": "Girona", "position": "DEL"}
    ]},
    {"name": "Noruega", "flag": "🇳🇴", "confed": "UEFA", "players": [
        {"name": "Ørjan Nyland", "number": 1, "club": "Sevilla", "position": "POR"},
        {"name": "Leo Østigård", "number": 3, "club": "Napoli", "position": "DEF"},
        {"name": "Sander Berge", "number": 8, "club": "Burnley", "position": "MED"},
        {"name": "Martin Ødegaard", "number": 10, "club": "Arsenal", "position": "MED"},
        {"name": "Erling Haaland", "number": 9, "club": "Man City", "position": "DEL"}
    ]},

    # CAF
    {"name": "Marruecos", "flag": "🇲🇦", "confed": "CAF", "players": [
        {"name": "Yassine Bounou", "number": 1, "club": "Al-Hilal", "position": "POR"},
        {"name": "Achraf Hakimi", "number": 2, "club": "PSG", "position": "DEF"},
        {"name": "Sofyan Amrabat", "number": 4, "club": "Man United", "position": "MED"},
        {"name": "Brahim Díaz", "number": 10, "club": "Real Madrid", "position": "MED"},
        {"name": "Youssef En-Nesyri", "number": 19, "club": "Sevilla", "position": "DEL"}
    ]},
    {"name": "Senegal", "flag": "🇸🇳", "confed": "CAF", "players": [
        {"name": "Édouard Mendy", "number": 16, "club": "Al-Ahli", "position": "POR"},
        {"name": "Kalidou Koulibaly", "number": 3, "club": "Al-Hilal", "position": "DEF"},
        {"name": "Pape Matar Sarr", "number": 17, "club": "Tottenham", "position": "MED"},
        {"name": "Sadio Mané", "number": 10, "club": "Al-Nassr", "position": "DEL"},
        {"name": "Nicolas Jackson", "number": 9, "club": "Chelsea", "position": "DEL"}
    ]},
    {"name": "Nigeria", "flag": "🇳🇬", "confed": "CAF", "players": [
        {"name": "Stanley Nwabali", "number": 1, "club": "Chippa United", "position": "POR"},
        {"name": "William Troost-Ekong", "number": 5, "club": "PAOK", "position": "DEF"},
        {"name": "Alex Iwobi", "number": 17, "club": "Fulham", "position": "MED"},
        {"name": "Ademola Lookman", "number": 11, "club": "Atalanta", "position": "DEL"},
        {"name": "Victor Osimhen", "number": 9, "club": "Napoli", "position": "DEL"}
    ]},
    {"name": "Egipto", "flag": "🇪🇬", "confed": "CAF", "players": [
        {"name": "Mohamed El Shenawy", "number": 1, "club": "Al Ahly", "position": "POR"},
        {"name": "Ahmed Hegazi", "number": 6, "club": "Al-Ittihad", "position": "DEF"},
        {"name": "Mohamed Elneny", "number": 17, "club": "Arsenal", "position": "MED"},
        {"name": "Omar Marmoush", "number": 22, "club": "Eintracht Frankfurt", "position": "DEL"},
        {"name": "Mohamed Salah", "number": 10, "club": "Liverpool", "position": "DEL"}
    ]},
    {"name": "Costa de Marfil", "flag": "🇨🇮", "confed": "CAF", "players": [
        {"name": "Yahia Fofana", "number": 1, "club": "Angers", "position": "POR"},
        {"name": "Evan Ndicka", "number": 5, "club": "Roma", "position": "DEF"},
        {"name": "Franck Kessié", "number": 8, "club": "Al-Ahli", "position": "MED"},
        {"name": "Seko Fofana", "number": 6, "club": "Al-Nassr", "position": "MED"},
        {"name": "Sébastien Haller", "number": 22, "club": "Dortmund", "position": "DEL"}
    ]},
    {"name": "Camerún", "flag": "🇨🇲", "confed": "CAF", "players": [
        {"name": "André Onana", "number": 24, "club": "Man United", "position": "POR"},
        {"name": "Jean-Charles Castelletto", "number": 21, "club": "Nantes", "position": "DEF"},
        {"name": "André-Frank Zambo Anguissa", "number": 8, "club": "Napoli", "position": "MED"},
        {"name": "Bryan Mbeumo", "number": 20, "club": "Brentford", "position": "DEL"},
        {"name": "Vincent Aboubakar", "number": 10, "club": "Beşiktaş", "position": "DEL"}
    ]},
    {"name": "Ghana", "flag": "🇬🇭", "confed": "CAF", "players": [
        {"name": "Lawrence Ati-Zigi", "number": 1, "club": "St. Gallen", "position": "POR"},
        {"name": "Mohammed Salisu", "number": 4, "club": "Monaco", "position": "DEF"},
        {"name": "Thomas Partey", "number": 5, "club": "Arsenal", "position": "MED"},
        {"name": "Mohammed Kudus", "number": 20, "club": "West Ham", "position": "MED"},
        {"name": "Iñaki Williams", "number": 19, "club": "Athletic Club", "position": "DEL"}
    ]},
    {"name": "Argelia", "flag": "🇩🇿", "confed": "CAF", "players": [
        {"name": "Anthony Mandrea", "number": 16, "club": "Caen", "position": "POR"},
        {"name": "Ramy Bensebaini", "number": 21, "club": "Dortmund", "position": "DEF"},
        {"name": "Ismaël Bennacer", "number": 22, "club": "AC Milan", "position": "MED"},
        {"name": "Houssem Aouar", "number": 8, "club": "Roma", "position": "MED"},
        {"name": "Riyad Mahrez", "number": 7, "club": "Al-Ahli", "position": "DEL"}
    ]},
    {"name": "Sudáfrica", "flag": "🇿🇦", "confed": "CAF", "players": [
        {"name": "Ronwen Williams", "number": 1, "club": "Mamelodi Sundowns", "position": "POR"},
        {"name": "Mothobi Mvala", "number": 14, "club": "Mamelodi Sundowns", "position": "DEF"},
        {"name": "Teboho Mokoena", "number": 4, "club": "Mamelodi Sundowns", "position": "MED"},
        {"name": "Themba Zwane", "number": 11, "club": "Mamelodi Sundowns", "position": "MED"},
        {"name": "Percy Tau", "number": 10, "club": "Al Ahly", "position": "DEL"}
    ]},

    # AFC
    {"name": "Japón", "flag": "🇯🇵", "confed": "AFC", "players": [
        {"name": "Zion Suzuki", "number": 23, "club": "Sint-Truiden", "position": "POR"},
        {"name": "Takehiro Tomiyasu", "number": 16, "club": "Arsenal", "position": "DEF"},
        {"name": "Wataru Endo", "number": 6, "club": "Liverpool", "position": "MED"},
        {"name": "Takefusa Kubo", "number": 20, "club": "Real Sociedad", "position": "MED"},
        {"name": "Kaoru Mitoma", "number": 7, "club": "Brighton", "position": "DEL"}
    ]},
    {"name": "Corea del Sur", "flag": "🇰🇷", "confed": "AFC", "players": [
        {"name": "Jo Hyeon-woo", "number": 21, "club": "Ulsan HD", "position": "POR"},
        {"name": "Kim Min-jae", "number": 4, "club": "Bayern Munich", "position": "DEF"},
        {"name": "Hwang In-beom", "number": 6, "club": "Crvena zvezda", "position": "MED"},
        {"name": "Lee Kang-in", "number": 18, "club": "PSG", "position": "MED"},
        {"name": "Son Heung-min", "number": 7, "club": "Tottenham", "position": "DEL"}
    ]},
    {"name": "Irán", "flag": "🇮🇷", "confed": "AFC", "players": [
        {"name": "Alireza Beiranvand", "number": 1, "club": "Persepolis", "position": "POR"},
        {"name": "Hossein Kanaanizadegan", "number": 13, "club": "Persepolis", "position": "DEF"},
        {"name": "Saeid Ezatolahi", "number": 6, "club": "Shabab Al-Ahli", "position": "MED"},
        {"name": "Sardar Azmoun", "number": 20, "club": "Roma", "position": "DEL"},
        {"name": "Mehdi Taremi", "number": 9, "club": "Porto", "position": "DEL"}
    ]},
    {"name": "Arabia Saudita", "flag": "🇸🇦", "confed": "AFC", "players": [
        {"name": "Mohammed Al-Owais", "number": 21, "club": "Al-Hilal", "position": "POR"},
        {"name": "Ali Al-Bulaihi", "number": 5, "club": "Al-Hilal", "position": "DEF"},
        {"name": "Mohamed Kanno", "number": 23, "club": "Al-Hilal", "position": "MED"},
        {"name": "Salem Al-Dawsari", "number": 10, "club": "Al-Hilal", "position": "MED"},
        {"name": "Firas Al-Buraikan", "number": 9, "club": "Al-Ahli", "position": "DEL"}
    ]},
    {"name": "Australia", "flag": "🇦🇺", "confed": "AFC", "players": [
        {"name": "Mathew Ryan", "number": 1, "club": "AZ Alkmaar", "position": "POR"},
        {"name": "Harry Souttar", "number": 19, "club": "Leicester City", "position": "DEF"},
        {"name": "Jackson Irvine", "number": 22, "club": "St. Pauli", "position": "MED"},
        {"name": "Craig Goodwin", "number": 23, "club": "Al-Wehda", "position": "MED"},
        {"name": "Mitchell Duke", "number": 15, "club": "Machida Zelvia", "position": "DEL"}
    ]},
    {"name": "Iraq", "flag": "🇮🇶", "confed": "AFC", "players": [
        {"name": "Jalal Hassan", "number": 1, "club": "Al-Zawraa", "position": "POR"},
        {"name": "Rebin Sulaka", "number": 2, "club": "FC Seoul", "position": "DEF"},
        {"name": "Amir Al-Ammari", "number": 16, "club": "Halmstads BK", "position": "MED"},
        {"name": "Ali Jasim", "number": 17, "club": "Al-Quwa Al-Jawiya", "position": "MED"},
        {"name": "Aymen Hussein", "number": 18, "club": "Al-Quwa Al-Jawiya", "position": "DEL"}
    ]},
    {"name": "Uzbekistán", "flag": "🇺🇿", "confed": "AFC", "players": [
        {"name": "Utkir Yusupov", "number": 1, "club": "Navbahor", "position": "POR"},
        {"name": "Abdukodir Khusanov", "number": 25, "club": "Lens", "position": "DEF"},
        {"name": "Otabek Shukurov", "number": 9, "club": "Kayserispor", "position": "MED"},
        {"name": "Jaloliddin Masharipov", "number": 10, "club": "Esteghlal", "position": "MED"},
        {"name": "Eldor Shomurodov", "number": 14, "club": "Cagliari", "position": "DEL"}
    ]},
    {"name": "Indonesia", "flag": "🇮🇩", "confed": "AFC", "players": [
        {"name": "Ernando Ari", "number": 21, "club": "Persebaya", "position": "POR"},
        {"name": "Jordi Amat", "number": 4, "club": "Johor Darul Ta'zim", "position": "DEF"},
        {"name": "Ivar Jenner", "number": 24, "club": "Utrecht", "position": "MED"},
        {"name": "Marselino Ferdinan", "number": 7, "club": "KMSK Deinze", "position": "MED"},
        {"name": "Rafael Struick", "number": 11, "club": "ADO Den Haag", "position": "DEL"}
    ]},

    # CONCACAF
    {"name": "Estados Unidos", "flag": "🇺🇸", "confed": "CONCACAF", "players": [
        {"name": "Matt Turner", "number": 1, "club": "Nottm Forest", "position": "POR"},
        {"name": "Antonee Robinson", "number": 5, "club": "Fulham", "position": "DEF"},
        {"name": "Weston McKennie", "number": 8, "club": "Juventus", "position": "MED"},
        {"name": "Tyler Adams", "number": 4, "club": "Bournemouth", "position": "MED"},
        {"name": "Christian Pulisic", "number": 10, "club": "AC Milan", "position": "DEL"}
    ]},
    {"name": "México", "flag": "🇲🇽", "confed": "CONCACAF", "players": [
        {"name": "Guillermo Ochoa", "number": 13, "club": "Salernitana", "position": "POR"},
        {"name": "César Montes", "number": 3, "club": "Almería", "position": "DEF"},
        {"name": "Edson Álvarez", "number": 4, "club": "West Ham", "position": "MED"},
        {"name": "Hirving Lozano", "number": 22, "club": "PSV", "position": "DEL"},
        {"name": "Santiago Giménez", "number": 11, "club": "Feyenoord", "position": "DEL"}
    ]},
    {"name": "Canadá", "flag": "🇨🇦", "confed": "CONCACAF", "players": [
        {"name": "Maxime Crépeau", "number": 16, "club": "Portland Timbers", "position": "POR"},
        {"name": "Alistair Johnston", "number": 2, "club": "Celtic", "position": "DEF"},
        {"name": "Stephen Eustáquio", "number": 7, "club": "Porto", "position": "MED"},
        {"name": "Alphonso Davies", "number": 19, "club": "Bayern Munich", "position": "DEF"},
        {"name": "Jonathan David", "number": 20, "club": "Lille", "position": "DEL"}
    ]},
    {"name": "Panamá", "flag": "🇵🇦", "confed": "CONCACAF", "players": [
        {"name": "Orlando Mosquera", "number": 22, "club": "Maccabi Tel Aviv", "position": "POR"},
        {"name": "Fidel Escobar", "number": 4, "club": "Saprissa", "position": "DEF"},
        {"name": "Adalberto Carrasquilla", "number": 8, "club": "Houston Dynamo", "position": "MED"},
        {"name": "Edgar Bárcenas", "number": 10, "club": "Mazatlán", "position": "MED"},
        {"name": "José Fajardo", "number": 17, "club": "U. Católica", "position": "DEL"}
    ]},
    {"name": "Jamaica", "flag": "🇯🇲", "confed": "CONCACAF", "players": [
        {"name": "Andre Blake", "number": 1, "club": "Philadelphia Union", "position": "POR"},
        {"name": "Ethan Pinnock", "number": 5, "club": "Brentford", "position": "DEF"},
        {"name": "Joel Latibeaudiere", "number": 22, "club": "Coventry City", "position": "DEF"},
        {"name": "Leon Bailey", "number": 9, "club": "Aston Villa", "position": "DEL"},
        {"name": "Michail Antonio", "number": 18, "club": "West Ham", "position": "DEL"}
    ]},
    {"name": "Honduras", "flag": "🇭🇳", "confed": "CONCACAF", "players": [
        {"name": "Edrick Menjívar", "number": 1, "club": "Olimpia", "position": "POR"},
        {"name": "Denil Maldonado", "number": 2, "club": "U Craiova", "position": "DEF"},
        {"name": "Deiby Flores", "number": 20, "club": "Toronto FC", "position": "MED"},
        {"name": "Luis Palma", "number": 7, "club": "Celtic", "position": "DEL"},
        {"name": "Anthony Lozano", "number": 9, "club": "Almería", "position": "DEL"}
    ]},
    {"name": "Costa Rica", "flag": "🇨🇷", "confed": "CONCACAF", "players": [
        {"name": "Keylor Navas", "number": 1, "club": "PSG", "position": "POR"},
        {"name": "Francisco Calvo", "number": 15, "club": "Juárez", "position": "DEF"},
        {"name": "Orlando Galo", "number": 14, "club": "Herediano", "position": "MED"},
        {"name": "Joel Campbell", "number": 12, "club": "Alajuelense", "position": "DEL"},
        {"name": "Manfred Ugalde", "number": 9, "club": "Spartak Moscow", "position": "DEL"}
    ]},

    # OFC
    {"name": "Nueva Zelanda", "flag": "🇳🇿", "confed": "OFC", "players": [
        {"name": "Max Crocombe", "number": 1, "club": "Burton Albion", "position": "POR"},
        {"name": "Liberato Cacace", "number": 13, "club": "Empoli", "position": "DEF"},
        {"name": "Marko Stamenić", "number": 8, "club": "Crvena zvezda", "position": "MED"},
        {"name": "Sarpreet Singh", "number": 10, "club": "Hansa Rostock", "position": "MED"},
        {"name": "Chris Wood", "number": 9, "club": "Nottm Forest", "position": "DEL"}
    ]}
]

@app.route('/')
def home():
    return render_template('index.html', history=history_data, teams=teams_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

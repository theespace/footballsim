import players
players.update_playerbase()

class Team:
    def __init__(self, name, wins, losses, division,
                 conference, team_roster, power, schedule,
                 team_stats, ovr_ranking, offensive_tendency,
                 defensive_tendency):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.division = division
        self.conference = conference
        self.team_roster = team_roster
        self.power = power
        self.schedule = schedule
        self.team_stats = team_stats
        self.ovr_ranking = ovr_ranking
        self.offensive_tendency = offensive_tendency
        self.defensive_tendency = defensive_tendency


all_teams = dict(
    # OFC
    # OFC North
    team1= Team("Chicago Mobsters", 0, 0, "OFC North", "OFC", players.rosters[0], 1, "Schedule1", "Statset1", 85,
                "Power Rushing", "Attacking"),
    team2= Team("Columbus Rockstars", 0, 0, "OFC North", "OFC", players.rosters[1], 2, "Schedule1", "Statset1", 80, "Air Raid",
                "Cover 3"),
    team3= Team("Toledo Glass Cannons", 0, 0, "OFC North", "OFC", players.rosters[2], 0, "Schedule1", "Statset1", 0, 0, 0),
    team4= Team("Fargo Runaways", 0, 0, "OFC North", "OFC", players.rosters[3], 0, "Schedule1", "Statset1", 0, 0, 0),
    # OFC East
    team5= Team("New York Slices", 0, 0, "OFC East", "OFC", players.rosters[4], 0, "Schedule1", "Statset1", 0, 0, 0),
    team6= Team("Boston Teabags", 0, 0, "OFC East", "OFC", players.rosters[5], 0, "Schedule1", "Statset1", 0, 0, 0),
    team7= Team("Raleigh Researchers", 0, 0, "OFC East", "OFC", players.rosters[6], 0, "Schedule1", "Statset1", 0, 0, 0),
    team8= Team("New Jersey Ragers", 0, 0, "OFC East", "OFC", players.rosters[7], 0, "Schedule1", "Statset1", 0, 0, 0),
    # OFC South
    team9= Team("Austin Startups", 0, 0, "OFC South", "OFC", players.rosters[8], 0, "Schedule1", "Statset1", 0, 0, 0),
    team10= Team("Tulsa Sirens", 0, 0, "OFC South", "OFC", players.rosters[9], 0, "Schedule1", "Statset1", 0, 0, 0),
    team11= Team("Mississippi Steamboats", 0, 0, "OFC South", "OFC", players.rosters[10], 0, "Schedule1", "Statset1", 0, 0, 0),
    team12= Team("Virginia Settlers", 0, 0, "OFC South", "OFC", players.rosters[11], 0, "Schedule1", "Statset1", 0, 0, 0),
    # OFC West
    team13= Team("Phoenix Burners", 0, 0, "OFC West", "OFC", players.rosters[12], 0, "Schedule1", "Statset1", 0, 0, 0),
    team14= Team("Boise Taters", 0, 0, "OFC West", "OFC", players.rosters[13], 0, "Schedule1", "Statset1", 0, 0, 0),
    team15= Team("San Jose Glitches", 0, 0, "OFC West", "OFC", players.rosters[14], 0, "Schedule1", "Statset1", 0, 0, 0),
    team16= Team("Spokane Rapids", 0, 0, "OFC West", "OFC", players.rosters[15], 0, "Schedule1", "Statset1", 0, 0, 0),

    # MFC
    # MFC North
    team17= Team("Montana Magic", 0, 0, "MFC North", "MFC", players.rosters[16], 0, "Schedule1", "Statset1", 0, 0, 0),
    team18= Team("Wisconsin Brewskis", 0, 0, "MFC North", "MFC", players.rosters[17], 0, "Schedule1", "Statset1", 0, 0, 0),
    team19= Team("Minnesota Penguins", 0, 0, "MFC North", "MFC", players.rosters[18], 0, "Schedule1", "Statset1", 0, 0, 0),
    team20= Team("Des Moines Defenders", 0, 0, "MFC North", "MFC", players.rosters[19], 0, "Schedule1", "Statset1", 0, 0, 0),
    # MFC East
    team21= Team("Philadelphia Fighters", 0, 0, "MFC East", "MFC", players.rosters[20], 0, "Schedule1", "Statset1", 0, 0, 0),
    team22= Team("Buffalo Tablesmashers", 0, 0, "MFC East", "MFC", players.rosters[21], 0, "Schedule1", "Statset1", 0, 0, 0),
    team23= Team("Bangor Claws", 0, 0, "MFC East", "MFC", players.rosters[22], 0, "Schedule1", "Statset1", 0, 0, 0),
    team24= Team("Baltimore Brewmasters", 0, 0, "MFC East", "MFC", players.rosters[23], 0, "Schedule1", "Statset1", 0, 0, 0),
    # MFC South
    team25= Team("Indianapolis Lefties", 0, 0, "MFC South", "MFC", players.rosters[24], 0, "Schedule1", "Statset1", 0, 0, 0),
    team26= Team("Chattanooga Catfish", 0, 0, "MFC South", "MFC", players.rosters[25], 0, "Schedule1", "Statset1", 0, 0, 0),
    team27= Team("Dallas Dust Devils", 0, 0, "MFC South", "MFC", players.rosters[26], 0, "Schedule1", "Statset1", 0, 0, 0),
    team28= Team("Georgia Chroniclers", 0, 0, "MFC South", "MFC", players.rosters[27], 0, "Schedule1", "Statset1", 0, 0, 0),
    # MFC West
    team29= Team("Los Angeles Culture", 0, 0, "MFC West", "MFC", players.rosters[28], 0, "Schedule1", "Statset1", 0, 0, 0),
    team30= Team("San Diego Sculpins", 0, 0, "MFC West", "MFC", players.rosters[29], 0, "Schedule1", "Statset1", 0, 0, 0),
    team31= Team("Alaska Mutts", 0, 0, "MFC West", "MFC", players.rosters[30], 0, "Schedule1", "Statset1", 0, 0, 0),
    team32= Team("Portland Hippies", 0, 0, "MFC West", "MFC", players.rosters[31], 0, "Schedule1", "Statset1", 0, 0, 0)
)

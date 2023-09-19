from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import os
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv('FANTASY_APP_ID')
client_id = os.getenv('FANTASY_CLIENT_ID')
client_secret = os.getenv('FANTASY_CLIENT_SECRET')

oauth = OAuth2(None, None, from_file='oauth2.json')

if not oauth.token_is_valid():
    oauth.refresh_access_token()

# Connect to the fantasy game
gm = yfa.Game(oauth, 'nfl')

# Connect to the league
league_id = gm.league_ids(year=2023)[0]
lg = gm.to_league(league_id)

teams = lg.teams()
team_table = {
    "ryan": "423.l.476888.t.1",
    "evan": "423.l.476888.t.2",
    "matthew": "423.l.476888.t.3",
    "brendan": "423.l.476888.t.4",
    "bobby": "423.l.476888.t.5",
    "matt": "423.l.476888.t.6",
    "dan": "423.l.476888.t.7",
    "kevin": "423.l.476888.t.8",
    "peter": "423.l.476888.t.9",
    "grant": "423.l.476888.t.10"
}

# Iterate over team_table
team_values = [value for value in team_table.values()]
# Get week 1 player data for each team
for team in team_values:
    print("### TEAM NAME: " + team + "###")
    team_players = lg.to_team(team).roster()
    player_ids = []
    for player in team_players:
        if player['selected_position'] == "QB":
            print("PLAYER QB: " + player['name'])
            week_1_stats = lg.player_stats(player["player_id"], "week", week=1)
            passing_points = week_1_stats[0]["Pass Yds"]/25
            passing_td_points = week_1_stats[0]["Pass TD"]*4
            interceptions = week_1_stats[0]["Int"]*-1
            rush_yd_points = week_1_stats[0]["Rush Yds"]/10
            fumbles = week_1_stats[0]["Fum Lost"]*-2
            total_pts = passing_points + passing_td_points + interceptions \
                + rush_yd_points + fumbles
            print("TOTAL POINTS: ", total_pts)
        if player['selected_position'] == "RB":
            print("PLAYER RB: " + player['name'])
            week_1_stats = lg.player_stats(player["player_id"], "week", week=1)
            passing_points = week_1_stats[0]["Pass Yds"]/25
            passing_td_points = week_1_stats[0]["Pass TD"]*4
            rushing_td_points = week_1_stats[0]["Rush TD"]*6
            interceptions = week_1_stats[0]["Int"]*-1
            rush_yd_points = week_1_stats[0]["Rush Yds"]/10
            fumbles = week_1_stats[0]["Fum Lost"]*-2
            total_pts = passing_points + passing_td_points + interceptions \
                + rush_yd_points + fumbles + rushing_td_points
            print("TOTAL POINTS: ", total_pts)
        if player['selected_position'] == "WR":
            print("PLAYER RB: " + player['name'])
            week_1_stats = lg.player_stats(player["player_id"], "week", week=1)
            passing_points = week_1_stats[0]["Pass Yds"]/25
            reception_yd_points = week_1_stats[0]["Rec Yds"]/10
            receiving_td_points = week_1_stats[0]["Rec TD"]*6
            passing_td_points = week_1_stats[0]["Pass TD"]*4
            rushing_td_points = week_1_stats[0]["Rush TD"]*6
            interceptions = week_1_stats[0]["Int"]*-1
            rush_yd_points = week_1_stats[0]["Rush Yds"]/10
            fumbles = week_1_stats[0]["Fum Lost"]*-2
            receptions = week_1_stats[0]["Rec"]/2
            total_pts = passing_points + passing_td_points + interceptions \
                + rush_yd_points + fumbles + rushing_td_points + receiving_td_points \
                + reception_yd_points + receptions
            print("TOTAL POINTS: ", total_pts)
        # player_ids.append(player['player_id'])
        # Calculate the amount of points scored
    

# my_players = lg.to_team("423.l.476888.t.4").roster()
# player_ids = []

# for player in my_players:
#     player_ids.append(player['player_id'])

print(player_ids)
print(lg.player_stats(player_ids, 'week', week=1))

# players = my_team.roster()

# for player in players:
#     print(player['name'])

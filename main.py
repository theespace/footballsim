# Teams
import teams
import players
import random
import statistics

# Game Variables
game_vars = dict(
    game_over=False,
    game_quarter=1,
    quarter_time=900,

    home_team=teams.all_teams["team1"],
    home_score=0,
    home_pass_yards=0,
    home_run_yards=0,
    home_kp=0,

    away_team=teams.all_teams["team2"],
    away_score=0,
    away_pass_yards=0,
    away_run_yards=0,
    away_kp=0,

    pass_td_scorers=[0],
    rush_td_scorers=[0],
    rec_td_scorers=[0],

    kicking_first=random.randint(0, 2),
    possession=0,
    los=25,
    down=1,
    distance=10
)


# Running a Play
def run_play():
    global game_vars
    play_time = 0
    personnel = [0, 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32]
    play_types = ["Rush", "Pass", "Trick", "Field Goal", "Punt", "Kneel"]
    defensive_play_styles = ["Rush","Pass","Trick","Field Goal","Punt","Blitz"]
    current_play_type = 0
    current_personnel = 0
    total_skill_players = 0
    if game_vars["possession"] == 0:
        offense = game_vars["home_team"]
        defense = game_vars["away_team"]

    #Offensive players
    possible_passers = [players.Player for players.Player in offense.team_roster.qbs]
    possible_ball_carriers = [players.Player for players.Player in offense.team_roster.qbs] \
                             + [players.Player for players.Player in offense.team_roster.hbs] \
                             + [players.Player for players.Player in offense.team_roster.fbs]
    possible_oline = dict(lts=[players.Player for players.Player in offense.team_roster.lts],
                          lgs=[players.Player for players.Player in offense.team_roster.lgs],
                          cs=[players.Player for players.Player in offense.team_roster.cs],
                          rgs=[players.Player for players.Player in offense.team_roster.rgs],
                          rts=[players.Player for players.Player in offense.team_roster.rts])
    possible_skill_players = dict(hbs=[players.Player for players.Player in offense.team_roster.hbs],
                                  fb=[players.Player for players.Player in offense.team_roster.fbs],
                                  tes=[players.Player for players.Player in offense.team_roster.tes],
                                  wrs=[players.Player for players.Player in offense.team_roster.wrs])
    oline = [possible_oline["lgs"][0], possible_oline["lgs"][0],
             possible_oline["cs"][0], possible_oline["rgs"][0],
             possible_oline["rts"][0]]
    passer = possible_passers[0]

    #Defensive players
    possible_left_side_d = [players.Player for players.Player in defense.team_roster.les] \
                             + [players.Player for players.Player in defense.team_roster.edges] \
                             + [players.Player for players.Player in defense.team_roster.lolbs] \
                             + [players.Player for players.Player in defense.team_roster.mlbs] \
                             + [players.Player for players.Player in defense.team_roster.cbs] \
                             + [players.Player for players.Player in defense.team_roster.fss]
    possible_middle_d = [players.Player for players.Player in defense.team_roster.dts] \
                             + [players.Player for players.Player in defense.team_roster.lolbs] \
                             + [players.Player for players.Player in defense.team_roster.mlbs] \
                             + [players.Player for players.Player in defense.team_roster.rolbs] \
                             + [players.Player for players.Player in defense.team_roster.fss] \
                             + [players.Player for players.Player in defense.team_roster.sss]
    possible_right_side_d = [players.Player for players.Player in defense.team_roster.res] \
                             + [players.Player for players.Player in defense.team_roster.edges] \
                             + [players.Player for players.Player in defense.team_roster.rolbs] \
                             + [players.Player for players.Player in defense.team_roster.mlbs] \
                             + [players.Player for players.Player in defense.team_roster.cbs] \
                             + [players.Player for players.Player in defense.team_roster.sss]
    possible_pass_d =  [players.Player for players.Player in defense.team_roster.lolbs] \
                             + [players.Player for players.Player in defense.team_roster.mlbs] \
                             + [players.Player for players.Player in defense.team_roster.rolbs] \
                             + [players.Player for players.Player in defense.team_roster.cbs] \
                             + [players.Player for players.Player in defense.team_roster.fss] \
                             + [players.Player for players.Player in defense.team_roster.sss]

    # Determine personnel and play type
    if offense.offensive_tendency == "Power Rushing":
        if game_vars["down"] == 1 and game_vars["distance"] == 10:
            current_personnel = int(
                list(random.choices(personnel, weights=(1, 1, 1, 1, 1, 5, 10, 3, 3, 5, 4, 2, 1, 1, 1), k=1))[0])
            current_personnel = 11
            if current_personnel == 0:
                ball_carrier = possible_passers[0]
                while total_skill_players < 5:
                    skill_players = random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1), k=5)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(20, 70, 10, 0, 0, 0), k=1)
            elif current_personnel == 1:
                ball_carrier = possible_passers[0]
                while total_skill_players < 5:
                    skill_players = random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=1) \
                                    + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1), k=4)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(25, 70, 5, 0, 0, 0), k=1)
            elif current_personnel == 2:
                ball_carrier = possible_passers[0]
                while total_skill_players < 5:
                    skill_players = random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=2) \
                                    + random.choices(possible_skill_players["wrs"], k=3)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(25, 70, 5, 0, 0, 0), k=1)
            elif current_personnel == 3:
                ball_carrier = possible_passers[0]
                while total_skill_players < 5:
                    skill_players = possible_skill_players["tes"] \
                                    + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1), k=2)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(50, 45, 5, 0, 0, 0), k=1)
            elif current_personnel == 10:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(15, 0, 78, 15, 5, 2), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 2), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=4)
                    else:
                        skill_players = [ball_carrier] + random.choices(possible_skill_players["wrs"], k=4)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(69, 30, 1, 0, 0, 0), k=1)
            elif current_personnel == 11:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(15, 0, 78, 15, 5, 2), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 2), k=1) \
                                        + random.choices(possible_skill_players["tes"], weights=(75, 20, 5), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=3)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_skill_players["tes"], weights=(75, 20, 5), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=3)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(69, 30, 1, 0, 0, 0), k=1)
            elif current_personnel == 12:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(15, 0, 78, 15, 5, 2), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 2), k=1) \
                                        + random.choices(possible_skill_players["tes"], weights=(75, 20, 5), k=2) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=2)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_skill_players["tes"], weights=(75, 20, 5), k=2) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=2)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(69, 30, 1, 0, 0, 0), k=1)
            elif current_personnel == 13:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(15, 0, 78, 15, 5, 2), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 2), k=1) \
                                        + possible_skill_players["tes"] \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=1)
                    else:
                        skill_players = [ball_carrier] \
                                        + possible_skill_players["tes"] \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=1)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(80, 19, 1, 0, 0, 0), k=1)
            elif current_personnel == 20:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(15, 0, 50, 30, 15, 15), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=2) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=3)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=3)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(50, 30, 10, 0, 0, 0), k=1)
            elif current_personnel == 21:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(5, 0, 78, 15, 5, 5), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 2), k=2) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=2)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 2), k=1) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=2)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(80, 19, 1, 0, 0, 0), k=1)
            elif current_personnel == 22:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(5, 0, 78, 15, 5, 15), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=2) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=2) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=1)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=1) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=2) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=1)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(80, 19, 1, 0, 0, 0), k=1)
            elif current_personnel == 23:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(5, 0, 78, 15, 5, 15), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=2) \
                                        + possible_skill_players["tes"]
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=1) \
                                        + possible_skill_players["tes"]
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(90, 9, 1, 0, 0, 0), k=1)
            elif current_personnel == 30:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(20, 0, 50, 50, 30, 50), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 78, 30, 5, 50), k=3) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=2)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 78, 15, 5, 50), k=2) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=2)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(70, 20, 10, 0, 0, 0), k=1)
            elif current_personnel == 31:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(10, 0, 60, 50, 50, 30), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 60, 50, 50, 50), k=3) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=1)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 60, 50, 50, 50), k=2) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=1) \
                                        + random.choices(possible_skill_players["wrs"], weights=(10, 8, 6, 4, 2, 1),
                                                         k=1)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(70, 20, 10, 0, 0, 0), k=1)
            elif current_personnel == 32:
                selected_ball_carrier = random.choices(possible_ball_carriers, weights=(5, 0, 60, 50, 50, 50), k=1)
                ball_carrier = selected_ball_carrier[0]
                while total_skill_players < 5:
                    if ball_carrier.position == "qb":
                        skill_players = random.choices(possible_ball_carriers, weights=(0, 0, 60, 50, 50, 50), k=3) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=2)
                    else:
                        skill_players = [ball_carrier] \
                                        + random.choices(possible_ball_carriers, weights=(0, 0, 60, 50, 50, 50), k=2) \
                                        + random.choices(possible_skill_players["tes"], weights=(70, 20, 10), k=2)
                    total_skill_players = len(list(dict.fromkeys(skill_players)))
                current_play_type = random.choices(play_types, weights=(90, 9, 1, 0, 0, 0), k=1)
            target_wr = random.choice(skill_players)
            blockers = oline
            blocking_power = statistics.mean([players.Player.ovr_rating for players.Player in blockers])
            print(current_personnel)
            print(current_play_type)
            print([players.Player.position + " " + players.Player.full_name for players.Player in skill_players])

    if defense.defensive_tendency == "Cover 3":
        if current_personnel == 11:
            left_side = random.choices(possible_left_side_d,weights=(10,2,10,2,8,1,10,5,1,10,5,3,1,1,1,10,1),k=5)
            middle_d = random.choices(possible_middle_d,weights=(10,8,3,3,1,10,8,3,3,1,3,1,3,1),k=5)
            right_side = random.choices(possible_right_side_d,weights=(10,2,10,2,8,1,10,5,1,10,5,3,1,1,1,10,1),k=5)
            pass_d = random.choices(possible_pass_d,weights=(3,1,10,5,1,3,1,10,10,8,3,1,1,10,2,10,2))
        all_d = left_side + middle_d + right_side + pass_d
        left_d_power = statistics.mean([players.Player.ovr_rating for players.Player in left_side])
        middle_d_power = statistics.mean([players.Player.ovr_rating for players.Player in middle_d])
        right_d_power = statistics.mean([players.Player.ovr_rating for players.Player in right_side])
        pass_d_power = statistics.mean([players.Player.ovr_rating for players.Player in pass_d])

    if current_play_type == ['Rush']:
        run_direction = ['left','middle','right']
        current_run_direction = random.choice(run_direction)
        hb_run_types = ['handoff','toss']
        qb_run_types = ['draw', 'keeper','scramble']
        if current_run_direction == 'middle':
            if ball_carrier.position == 'qb':
                current_run_type = 'draw'
            current_run_type = 'handoff'
            print(ball_carrier.full_name + ' takes the ' + current_run_type + ' up the ' + current_run_direction + '...')
            play_winner_odds = ['o'] * (int(blocking_power) ** 2) + ['d'] * (int(middle_d_power) ** 2)
            play_winner = random.choice(play_winner_odds)
            tackler = random.choice(middle_d)
        elif current_run_direction == 'left':
            current_run_type = random.choice(hb_run_types)
            print(ball_carrier.full_name + ' takes the ' + current_run_type + ' to the ' + current_run_direction + '...')
            play_winner_odds = ['o'] * (int(blocking_power) ** 2) + ['d'] * (int(left_d_power) ** 2)
            play_winner = random.choice(play_winner_odds)
            tackler = random.choice(left_side)
        elif current_run_direction == 'right':
            current_run_type = random.choice(hb_run_types)
            print(ball_carrier.full_name + ' takes the ' + current_run_type + ' to the ' + current_run_direction + '...')
            play_winner_odds = ['o'] * (int(blocking_power) ** 2) + ['d'] * (int(right_d_power) ** 2)
            play_winner = random.choice(play_winner_odds)
            tackler = random.choice(right_side)
        if play_winner == 'o':
            possible_results = ['small gain'] * 10 + ['medium gain'] * 5 \
                               + ['large gain'] * 2 + ['huge gain']
            play_result = random.choice(possible_results)
            if play_result == 'small gain':
                yardage = random.randint(1, 4)
                print('... for a gain of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'medium gain':
                yardage = random.randint(4, 8)
                print('... for a gain of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'large gain':
                yardage = random.randint(8, 20)
                print('... for a big gain of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'huge gain':
                yardage = random.randint(20, 100)
                print('... for a HUGE gain of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
        if play_winner == 'd':
            possible_results = ['no gain'] * 15 + ['small loss'] * 10 \
                               + ['medium loss'] * 5 + ['large loss'] + ['fumble']
            play_result = random.choice(possible_results)
            if play_result == 'no gain':
                yardage = 0
                print('... and tackled for no gain. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'small loss':
                yardage = random.randint(1, 4)
                print('... for a loss of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'medium loss':
                yardage = random.randint(4, 8)
                print('... for a big loss of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'large loss':
                yardage = random.randint(8, 20)
                print('... for a HUGE loss of ' + str(yardage) + ' yards. (Tackled by #' + str(
                    tackler.number) + ' ' + tackler.full_name + ')')
            if play_result == 'fumble':
                ball_recovered_by = random.choice(all_d)
                yardage_before_fumble = random.randint(0, 100-game_vars['los'])
                yardage = yardage_before_fumble - random.randint(0, yardage_before_fumble)
                print('... FUMBLE! Forced by #' + str(
                    tackler.number) + ' ' + tackler.full_name + '. Recovered by #'
                    + ball_recovered_by.number + ' ' + ball_recovered_by.full_name + ' for '
                    + str(yardage) + ' yards.')
                if game_vars['possession'] == 0:
                    game_vars['possession'] = 1
                if game_vars['possession'] == 1:
                    game_vars['possession'] = 0





    elif current_play_type == ['Pass']:
        passer = possible_passers[0]
        print(passer.full_name + " drops back...")


run_play()
run_play()
run_play()
run_play()
run_play()
run_play()
run_play()
run_play()
run_play()
run_play()
run_play()
run_play()

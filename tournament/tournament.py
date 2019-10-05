from collections import Counter, defaultdict

TEMPLATE = '{:<31}|{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'


def tally(tournament_results):
    tournament_table = generate_results(tournament_results)
    results = [TEMPLATE.format('Team', 'MP', 'W', 'D', 'L', 'P')]

    for team, result in tournament_table:
        results.append(TEMPLATE.format(team, result['MP'], result['W'],
                                       result['D'], result['L'], result['P']))
    return '\n'.join(results)


def generate_results(input_data):

    tournament_table = defaultdict(Counter)
    result_map = {"win": "loss", "loss": "win", "draw": "draw"}
    points_map = {"win": 3, "loss": 0, "draw": 1}
    for line in input_data.splitlines():
        lines = [line.split(";")]
        for home, away, result in lines:
            tournament_table[home][result] += 1
            tournament_table[away][result_map[result]] += 1

        for team, results in tournament_table.items():
            tournament_table[team]['MP'] = results['win'] + results['loss'] + results['draw']
            tournament_table[team]['P'] = results['win']*points_map['win'] + results['draw']*points_map['draw']
            tournament_table[team]['W'] = results['win']
            tournament_table[team]['L'] = results['loss']
            tournament_table[team]['D'] = results['draw']

    return sort_tournament_table(tournament_table)


def sort_tournament_table(tournament_table):
    sorted_table = sorted(tournament_table.items(), key=lambda kv: kv[0])
    return sorted(sorted_table, key=lambda tup: tup[1]['P'], reverse=True)

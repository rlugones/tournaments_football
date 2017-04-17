from Team import Team

class Group(object):
  """
  Tournament group class.
  """
  def __init__(self, name_group, list_of_teams, ppm):
    self.name = name_group
    self.teams = list_of_teams
    self.team_names = []
    for i in self.teams: self.team_names.append(i.name)
    [self.pwin, self.pdraw, self.plose] = ppm

  def __str__(self):
    return self.name

  def read_match(self, match):
    """Analize a match"""
    match = match.split('#')[0]
    team1g = int(match.split('-')[0].split(' ')[-1])
    team1 = match.split('-')[0][:-len(str(team1g))-1]
    team2g = int(match.split('-')[1].split(' ')[0])
    team2 = ' '.join(match.split('-')[1][len(str(team2g))+1:].split())
    try:
      team1 = self.teams[self.team_names.index(team1)]
      team2 = self.teams[self.team_names.index(team2)]
    except:
      return 1
    team1.update_goalsfa(team1g, team2g)
    team2.update_goalsfa(team2g, team1g)
    if team1g > team2g:
      team1.match_won()
      team2.match_lost()
    elif team2g > team1g:
      team1.match_lost()
      team2.match_won()
    else:
      team1.match_draw()
      team2.match_draw()
    team1.update_team(self)
    team2.update_team(self)
    return 0

  def print_table(self):
    """ Create table of the tournament"""
    name_len = 0
    for team in self.teams: name_len = max(name_len, len(team.name))
    print('{:<{width}}'.format('Team', width=name_len+1),\
          '%-4s%-4s%-4s%-4s%-4s%-4s%-4s%-4s' % ('P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'))
    print('---------------------------------------------------------')
    teams_sorted = sorted(self.teams, key=lambda team: team.points, reverse=True)
    for i in teams_sorted:
      print('{:<{width}}'.format(i.name, width=name_len+1), '%-4i%-4i%-4i%-4i%-4i%-4i%-4i%-4i'\
            % (i.played, i.win, i.draw, i.lose, i.goalsfor, i.goalsagainst, i.goalsdifference,\
               i.points))

class Tournament(object):
  """
  Tournament group class.
  """
  def __init__(self, groups, file_results):
    self.groups = groups
    with open(file_results, 'r') as fresults: self.results = fresults.read().split('\n')
    self.results = [result for result in self.results if (result[:1] != '#' and result[:1] != '')]

  def read_allmatches(self):
    """Reads all the matches"""
    for group in self.groups:
      for match in self.results[:]:
        r = group.read_match(match)
        if r == 0: self.results.remove(match)

  def update_results(self):
    """Read the results of the matches played"""
    self.read_allmatches()
    #for i in self.groups: i.read_allmatches()

  def print_groups(self):
    """ Create table of the tournament"""
    name_len = 0
    for group in self.groups:
      print(group.name)
      for team in group.teams: name_len = max(name_len, len(team.name))
      print('{:<{width}}'.format('Team', width=name_len+1),\
            '%-4s%-4s%-4s%-4s%-4s%-4s%-4s%-4s' % ('P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts'))
      print('---------------------------------------------------------')
      teams_sorted = sorted(group.teams, key=lambda team: (team.points, team.goalsdifference),\
                            reverse=True)
      for i in teams_sorted:
        print('{:<{width}}'.format(i.name, width=name_len+1), '%-4i%-4i%-4i%-4i%-4i%-4i%-4i%-4i'\
              % (i.played, i.win, i.draw, i.lose, i.goalsfor, i.goalsagainst, i.goalsdifference,\
                 i.points))
      print()

    # Checks if there is match not included because of errors in the teams' names
    if self.results:
      print('Warning: matches not included:')
      for i in self.results: print(i)

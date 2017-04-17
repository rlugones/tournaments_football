class Team(object):
  """
  Football team class.
  """
  def __init__(self, name):
    self.name = name
    self.group = ''
    self.win = 0
    self.lose = 0
    self.draw = 0
    self.played = 0
    self.points = 0
    self.goalsfor = 0
    self.goalsagainst = 0
    self.goalsdifference = 0

  def __str__(self):
    return self.name

  def set_group(self, group):
    """Set group where the team will be"""
    self.group = group

  def calculate_points(self, group): #pwin=2, pdraw=1, plose=0):
    """Calculate points for a team"""
    self.points = self.win*group.pwin + self.draw*group.pdraw + self.lose*group.plose

  def calculate_goalsdifference(self):
    """Calculate points for a team"""
    self.goalsdifference = self.goalsfor - self.goalsagainst

  def calculate_matchesplayed(self):
    """Calculate matches played by a team"""
    self.played = self.win + self.draw + self.lose

  def match_won(self):
    """Update self.win"""
    self.win += 1

  def match_draw(self):
    """Update self.draw"""
    self.draw += 1

  def match_lost(self):
    """Update self.lose"""
    self.lose += 1

  def update_goalsfa(self, goalsfor, goalsagainst):
    """Update self.goalsfor and self.goalsagainst"""
    self.goalsfor += goalsfor
    self.goalsagainst += goalsagainst

  def update_team(self, group):
    """Runs all the methods necessaries to update all atributes of a team"""
    self.calculate_points(group)
    self.calculate_goalsdifference()
    self.calculate_matchesplayed()

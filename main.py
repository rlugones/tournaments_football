#!/usr/bin/env python3
##!/usr/bin/python3
##!/share/apps/python-3.4.3/bin/python3.4

"""
./main.py tournament

This program creates a round robin football tournament and prints the
current state of the groups.

Parameters
----------
tournament: str
  The name of the tournament.

Returns
-------
print on screen:
  Current state of the groups.

Examples
--------
./main.py ElFutbolazo

"""
import sys
from Team import Team
from Tournament import Tournament
from TournamentGroup import Group
from read_input import read_input

if __name__ == "__main__":
  #Reads the name of the tournament from prompt
  if len(sys.argv) != 2: sys.exit('### ERROR: Choose a tournament')
  nfile = sys.argv[1]

  #Reads the tournament details, the groups and the teams from the input file
  [teams_and_groups, file_results, ppm] = read_input(nfile)
  allteams = []
  allgroups = []
  nallgroups = set([])
  ngroup = 'NG'
  for i in teams_and_groups:
    if i[0:4] == '': ngroup = 'NG'
    elif i[0:4] == '### ':
      ngroup = i[4:]
      nallgroups.add(ngroup)
    else:
      allteams.append(Team(i))
      allteams[-1].set_group(ngroup)
  pointspermatch = [2, 1, 0]
  for i in sorted(nallgroups):
    allgroups.append(Group(i, [team for team in allteams if team.group == i], ppm))

  #Creates the tournament
  tournament = Tournament(allgroups, file_results)
  tournament.update_results()
  tournament.print_groups()

def read_input(ntournament):
  ftournament = open(ntournament, 'r')
  file_results = ftournament.readline().split()[0]
  pointswin = int(ftournament.readline().split()[0])
  pointsdraw = int(ftournament.readline().split()[0])
  pointslose = int(ftournament.readline().split()[0])
  ppm = [pointswin, pointsdraw, pointslose]
  teams_and_groups = []
  save_tag = 0
  for line in ftournament:
    if line.startswith('#####TEAMS_AND_GROUPS#####'): save_tag = 1
    if line.startswith('#####END TEAMS_AND_GROUPS#####'): break
    if save_tag: teams_and_groups.append(line[:-1])
  ftournament.close()
  return [teams_and_groups, file_results, ppm]

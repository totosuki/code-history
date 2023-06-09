def return_score(lines, collect_lines):
  score = 100
  for i, line in enumerate(lines):
    diff = abs(line - collect_lines[i])
    if diff <= 5:
      continue
    elif diff <= 10:
      score -= 1
      continue
    elif diff <= 20:
      score -= 2
    elif diff <= 30:
      score -= 3
    else:
      score -= 5
  if score < 0:
    score = 0
  return score


N, M = map(int, input().split())
collect_lines = []
for _ in range(M):
  collect_lines.append(int(input()))
player_lines = []
for _ in range(N):
  lines = []
  for __ in range(M):
    lines.append(int(input()))
  player_lines.append(lines)

scores = []
#main
for lines in player_lines:
  scores.append(return_score(lines, collect_lines))
print(max(scores))
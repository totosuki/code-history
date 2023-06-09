def clean_list(task_list, index):
  start_index = index
  now_index = index + 1
  max_day = task_list[start_index][1]
  flag = False
  while not flag:
    if now_index >= len(task_list):
      break
    if max_day >= task_list[now_index][0] - 1: #繋がっている日付の一番遅い日より２日以上遅い場合はelseに行く
      if max_day < task_list[now_index][1]: #繋がっている日付の一番遅い日が変わったならば変更
        max_day = task_list[now_index][1]
      now_index += 1
    else:
      flag = True
  return max_day - task_list[start_index][0] + 1, now_index

N = int(input())
task_list = []
for _ in range(N):
  task_list.append(list(map(int, input().split())))

sorted_tasks = sorted(task_list)
# print(sorted_tasks)

check_index = 0
rslt = []
#main
while check_index <= len(sorted_tasks) -1:
  dupe_day_task, check_index =  clean_list(sorted_tasks, check_index)
  rslt.append(dupe_day_task)
print(max(rslt))
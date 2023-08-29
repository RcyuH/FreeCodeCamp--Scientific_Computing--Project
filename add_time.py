#CONST
lst_rank = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thurday":4, "Friday":5,"Saturday":6, "Sunday":7}
lst_rank_reverse = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thurday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

#Function
def hours(timenow, timeplus):
  lst_hour = []
  i = timenow.split()
  j = i[0].split(":")
  lst_hour.append(int(j[0]))
  j = timeplus.split(":")
  lst_hour.append(int(j[0]))
  return lst_hour

def minutes(timenow, timeplus):
  lst_min = []
  i = timenow.split()
  j = i[0].split(":")
  lst_min.append(int(j[1]))
  j = timeplus.split(":")
  lst_min.append(int(j[1]))
  return lst_min

def am_or_pm(timenow):
  am_pm = timenow.split()[1]
  return am_pm

def search_rank(days, today):
  number_day = lst_rank[today[0]] + days
  if number_day > 7:
    number_day = number_day%7
  return lst_rank_reverse[number_day]

def display(hour_end, min_end, am_pm, days, *today):
  try:
    rank = search_rank(days, today)
    if min_end < 10:
      if days == 0:
        print(str(hour_end) + ":0" + str(min_end) + " " + am_pm + ", " + rank)
      elif days == 1:
        print(str(hour_end) + ":0" + str(min_end) + " " + am_pm + ", " + rank + " (next day)")
      else:
        print(str(hour_end) + ":0" + str(min_end) + " " + am_pm + ", " + rank + " (" + str(days) + " days later)")
    else:
      if days == 0:
        print(str(hour_end) + ":" + str(min_end) + " " + am_pm + ", " + rank)
      elif days == 1:
        print(str(hour_end) + ":" + str(min_end) + " " + am_pm + ", " + rank + " (next day)")
      else:
        print(str(hour_end) + ":" + str(min_end) + " " + am_pm + ", " + rank + " (" + str(days) + " days later)")
  except:
    if min_end < 10:
      if days == 0:
        print(str(hour_end) + ":0" + str(min_end) + " " + am_pm)
      elif days == 1:
        print(str(hour_end) + ":0" + str(min_end) + " " + am_pm + " (next day)")
      else:
        print(str(hour_end) + ":0" + str(min_end) + " " + am_pm + " (" + str(days) + " days later)")
    else:
      if days == 0:
        print(str(hour_end) + ":" + str(min_end) + " " + am_pm)
      elif days == 1:
        print(str(hour_end) + ":" + str(min_end) + " " + am_pm + " (next day)")
      else:
        print(str(hour_end) + ":" + str(min_end) + " " + am_pm + " (" + str(days) + " days later)")

def process(am_pm, lst_hour, lst_min, *today):
  days = int(lst_hour[1]/24) 
  hour_end = lst_hour[1]%24 + lst_hour[0]
  min_end = lst_min[0] + lst_min[1]
  if (lst_hour[1]%12)%2 != 0:
    if am_pm == "AM": am_pm == "PM"
    if am_pm == "PM": am_pm == "AM"
  if min_end >= 60:
    min_end = min_end - 60
    hour_end += 1
  if hour_end > 11:
    if am_pm == "PM":
      am_pm = "AM"
      days += 1
    else:
      am_pm = "PM"
  if hour_end > 12:
    hour_end -= 12
  display(hour_end, min_end, am_pm, days, *today)

def add_time(timenow, timeplus, *today):
  lst_hour = hours(timenow, timeplus)
  lst_min = minutes(timenow, timeplus)
  am_pm = am_or_pm(timenow)
  process(am_pm, lst_hour, lst_min, *today)

# Using readlines()
input_file = open('input.XSCORE', 'r')
lines = input_file.readlines()
  
calories = []
curr_cal = 0

# Strips the newline character
for line in lines:
    if line.isspace():
        # elf has changed we append curr_cal in array calories and reset curr_cal
        calories.append(curr_cal)
        curr_cal = 0
    else:
        # add line to curr_cal
        curr_cal += int(line)

calories.sort(reverse=True)
top3_calories = calories[0] + calories[1] + calories[2]

print(top3_calories)

# Using readlines()
input_file = open('input.XSCORE', 'r')
lines = input_file.readlines()
  
max_cal = 0
curr_cal = 0

# Strips the newline character
for line in lines:
    if line.isspace():
        # new elf - check whether curr_cal is > max_cal, if so then assign curr_cal to max_cal and reset curr_cal to 0
        if curr_cal > max_cal:
            max_cal = curr_cal
        curr_cal = 0
    else:
        # add line to curr_cal
        curr_cal += int(line)

print(max_cal)

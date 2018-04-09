import sys
def result(now_direction,turn):
    if turn=='L':
        if now_direction=='N':
            return 'W'
        elif now_direction=='S':
            return 'E'
        elif now_direction=='W':
            return 'S'
        else:
            return 'N'
    else:
        if now_direction=='N':
            return 'E'
        elif now_direction=='S':
            return 'W'
        elif now_direction=='W':
            return 'N'
        else:
            return 'S'
    
n = int(sys.stdin.readline().strip())
plans = list(sys.stdin.readline().strip())
now_direction = 'N'
for turn in plans:
    now_direction = result(now_direction,turn)

print (now_direction)



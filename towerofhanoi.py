def towerofHanoi(n, start, finish, aux):
    if n == 0:
        return
    towerofHanoi(n - 1, start, aux, finish)
    print("Move disk", n, "from rod", start, "to rod", finish)
    towerofHanoi(n - 1, aux, finish, start)

disks = 5
start = 'A'
aux = 'B'
finish = 'C'

towerofHanoi(disks, start, finish, aux)
score = 0
level = 1

while True:
    if score == 100 and level == 1:
        level += 1
        player.lives += 1
        score += 100
    elif score == 200 and level == 2:
        level += 1
        enemies.append(Boss(0, 0, 100))
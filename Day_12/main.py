################### Scope ####################

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Scope
# player_health = 10


# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()


# There is no Block Scope


# game_level = 3


# def create_enemy():
#     enemies = ["Skeleton", "Zombie"]
#     if game_level < 5:
#         new_enemy = enemies[0]


#     print(new_enemy)


# Global Constants
PI = 3.14159



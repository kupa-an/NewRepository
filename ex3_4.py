import random

def take_stones(player, stones):
    while True:
        try:
            num = int(input(f"Игрок {player}, введите количество камней (1-3): "))
            if 1 <= num <= 3 and num <= stones:
                return num
            else:
                print("Некорректный ввод. Введите число от 1 до 3, не превышающее количество оставшихся камней.")
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 3.")

stones = random.randint(4, 30)
player = "Пользователь"

while stones > 0:
    print(f"\nОсталось камней: {stones}")
    user_choice = take_stones(player, stones)
    stones -= user_choice

    player = "Компьютер"
    computer_choice = random.randint(1, min(3, stones))
    stones -= computer_choice
    print(f"\nКомпьютер взял {computer_choice} камней.")
    
    
    if stones == 1:
        print(f"\n{player} выиграл!")
        break

    if stones == 0:
        print("\nКомпьютер выиграл!")


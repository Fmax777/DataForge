import random
import time


def start_rpg_game():
    print("=== КВЕСТ: СПАСЕНИЕ ПРОДАКШЕНА ===")
    print("Вы — молодой Джуниор Дата-Инженер. В коде завелся страшный Баг!")
    print("Ваша задача — уничтожить его, пока не упали все сервера компании.\n")

    # Параметры персонажей
    player_hp = 100
    bug_hp = 80

    player_skills = {
        "1": ("Удар костылем (Обычная атака)", 12, 18),
        "2": ("Оптимизация кода (Критический урон, шанс промаха)", 5, 35),
        "3": ("Погуглить на StackOverflow (Лечение)", 15, 25)
    }

    while player_hp > 0 and bug_hp > 0:
        print(f"Ваше здоровье (Оптимизм): {player_hp} HP | Здоровье Бага: {bug_hp} HP")
        print("Выберите ваше действие:")
        for key, (name, _, _) in player_skills.items():
            print(f"{key}. {name}")

        choice = input("Введите номер хода: ").strip()
        print("-" * 40)

        if choice in ["1", "2"]:
            name, min_dmg, max_damage = player_skills[choice]
            damage = random.randint(min_dmg, max_damage)
            if choice == "2" and random.random() < 0.3:
                print("❌ Вы запутались в документации и промахнулись!")
                damage = 0
            else:
                print(f"⚔️ Вы применяете '{name}' и наносите Багу {damage} урона!")
                bug_hp -= damage
        elif choice == "3":
            name, min_heal, max_heal = player_skills[choice]
            heal = random.randint(min_heal, max_heal)
            player_hp += heal
            print(f"❤️ Вы нашли ответ на StackOverflow и восстановили {heal} HP!")
        else:
            print("🤔 Вы задумались и пропустили ход...")

        if bug_hp <= 0:
            break

        # Ход Бага
        time.sleep(1)
        bug_damage = random.randint(10, 22)
        player_hp -= bug_damage
        print(f"👾 Баг атакует в ответ! Ошибка 'NullPointerException' наносит вам {bug_damage} урона.\n")
        time.sleep(1)

    print("=========================================")
    if player_hp > 0:
        print("🎉 ПОБЕДА! Баг успешно исправлен. Сервера спасены, вас ждёт оффер на Мидла!")
    else:
        print("💀 ИГРА ОКОНЧЕНА. Продакшен упал, логи забиты ошибками. Придётся восстанавливать бэкапы.")
    print("=========================================")


if __name__ == "__main__":
    start_rpg_game()

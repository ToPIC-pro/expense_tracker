
import json
import os
from datetime import datetime

FILE = "expenses.json"


def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)


expenses = load_expenses()

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1. Добавить расход")
    print("2. История расходов")
    print("3. Общая сумма расходов")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Название расхода: ").strip()

        if not name:
            print("Название не может быть пустым!")
            continue

        try:
            amount = int(input("Сумма в рублях: "))

            if amount <= 0:
                print("Сумма должна быть больше нуля!")
                continue

        except ValueError:
            print("Введите целое число!")
            continue

        expenses.append({
            "name": name,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        save_expenses(expenses)
        print("Расход успешно добавлен!")

    elif choice == "2":
        if not expenses:
            print("История расходов пуста.")
        else:
            print("\nИстория расходов:")

            for i, expense in enumerate(expenses, 1):
                print(
                    f"{i}. {expense['name']} — "
                    f"{expense['amount']} руб. "
                    f"({expense['date']})"
                )

    elif choice == "3":
        total = sum(e["amount"] for e in expenses)
        print(f"Общая сумма расходов: {total} руб.")

    elif choice == "0":
        print("До свидания!")
        break

    else:
        print("Неизвестная команда!")

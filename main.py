import random

shop = {
    'cases': [
        {
            'name': 'gun_case',
            'items': ["AK-47", "AWP", "M4A4-S", "M4A4", "Desert Eagle", "Tec-9", "five-seven", "glock-19", "USP-S"],
            'price': 400,
        },
        {
            'name': 'knife_case',
            'items': ["Kerambit", "stilleto", "M9 bayonet", "Scorpion", "butterfly"],
            'price': 600,
        }
    ],
    'items': [
        {
            'name': 'AK-47',
            'price': 200,
        },
        {
            'name': 'AWP',
            'price': 600,
        },
        {
            'name': 'M4A4-S',
            'price': 300,
        },
        {
            'name': 'M4A4',
            'price': 200,
        },
        {
            'name': 'Desert Eagle',
            'price': 500,
        },
        {
            'name': 'Tec-9',
            'price': 300,
        },
        {
            'name': 'five-seven',
            'price': 230,
        },
        {
            'name': 'glock-19',
            'price': 150,
        },
        {
            'name': 'USP-S',
            'price': 300,
        },
        {
            'name': 'Kerambit',
            'price': 1000,
        },
        {
            'name': 'stilleto',
            'price': 1200,
        },
        {
            'name': 'Scorpion',
            'price': 1400,
        },
        {
            'name': 'M9 bayonet',
            'price': 1400,
        },
        {
            'name': 'butterfly',
            'price': 2000000,
        },

    ]

}

inventar = {
    'cases': [
        {
            'name': 'gun_case',
            'items': ["AK-47", "AWP", "M4A4-S", "M4A4", "Desert Eagle", "Tec-9", "five-seven", "glock-19", "USP-S"],
            'price': 400,
        }
    ],
    'items': []
}

balance = 1000
print('Добро пожаловать в симулятор открытия кейсов CS\n')


def open_case():
    if len(inventar['cases']) < 1:
        print('У тебя нет ни одного кейса(')
    else:
        for case_num, case in enumerate(inventar['cases']):
            print(f'[{case_num}] {case}')
        choice_case = int(input('Выбери кейс'))
        case = inventar['cases'].pop(choice_case)
        item = random.choice(case['items'])
        inventar['items'].append(item)
        print(f'Тебе выпл {item}!')


while True:
    print('[0] Выход\n'
          '[1] Открыть кейс\n'
          '[2] Инвентарь\n'
          '[3] Магазин\n'
          '[4] Проверить баланс\n')

    event = input('Выберите действие: ')

    if event == '0':
        print('Пока!')
        break
    elif event == '1':
        open_case()
    elif event == '2':
        print(f'--\n'
              f'{inventar}\n'
              f'--\n')
    elif event == '3':
        print('[0] - Купить\n'
              '[1] - Продать\n'
              '[-1] - Назад\n')
        shop_event = input('Выбери действие')
        if shop_event == '0':
            print('[0] - кейсы\n')
            choice_shop = input('Выбери действие')
            if choice_shop == '0':
                for case_num, case in enumerate(shop['cases']):
                    print(f'[{case_num}] {case}')
                choice_case = int(input('Выбери кейс'))
                case = shop['cases'].pop(choice_case)
                if balance >= case['price']:
                    inventar['cases'].append(case)
                    balance -= case['price']
                else:
                    print('Недостаточно средств')
        elif shop_event == '1':
            if len(inventar['items']) < 1:
                print('У тебя нет предметов на продажу')
            else:
                for case_num, case in enumerate(inventar['items']):
                    print(f'[{case_num}] {case}')
                choice_item = int(input('Выбери предмет на продажу'))
                item_ = inventar['items'].pop(choice_item)
                item_price = 0
                for item in shop['items']:
                    print(item)
                    print(item_)
                    if item['name'] == item_:
                        item_price = item['price']
                balance += item_price

    elif event == '4':
        print(balance)

    else:
        print('такое действие мы еще не придумали')

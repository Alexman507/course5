from entity.shop import Shop
from entity.store import Store

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "елка": 25
})

shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "елка": 2
})

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = (
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('стоп', 'stop'):
            break

        try:
            request = Request(request=user_input)
        except InvalidRequest as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        break


if __name__ == '__main__':
    main()

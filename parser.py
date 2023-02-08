import ccxt
import time


def start_check_xrp():
    """Не используются функции, try except и прочие вещи для ускорения кода, чтобы лишний раз
       не замедляться, не создавать новые объекты, вызовы и пр.(хотя тут для читебальности
       и целостности они бы не помешали"""
    binance = ccxt.binance()
    symbol = 'XRP/USDT'  # пару которую ищем
    check_interval = 60

    while True:
        ticker = binance.fetch_ticker(symbol)  # получаем словарь нашей пары
        price = ticker['last']  # последняя цена
        max_price = ticker['high']  # максимальная

        # Проверка, упала ли цена на 1% от максимальной цены за последний час
        if price < max_price * 0.99:
            print(f"Цена {symbol} упала на 1% от максимальной цены за последний час: {price}")

        time.sleep(check_interval)


if __name__ == "__main__":
    start_check_xrp()

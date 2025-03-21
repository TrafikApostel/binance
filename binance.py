rom binance.client import Client

api_key = "xxx"
api_secret = "xxx"

client = Client(api_key, api_secret)
symbol = "HBARUSDT"
latest_price = client.futures_symbol_ticker(symbol=symbol)['price']
latest_price = float(latest_price)
print(latest_price)

proc_bar_ok_1 = 0.6
proc_bar_ok_2 = 0.2
imb_long = 0.1
imb_short = 0.1

symbol = "BTCUSDT"

interval = "1m"

klines = client.futures_historical_klines(symbol,
                                          interval, start_str=None, end_str=None, limit=50)
opaopa = []
opaopa1 = []
print('----------')
print(klines)
print(klines[-1])
print('---------')
lst_3 = []
tri = 0
low1_tr = True
low2_tr = False
i = 1
r_klines = reversed(klines)
for item in r_klines:
    try:
        low = float(item[3])
        higt = float(klines[-i-2][2])
        if higt < low:
            opaopa.append({'high': higt, 'low': low, 'percent':low / (higt / 100)})
        higt1 = float(item[2])
        low1 = float(klines[-i - 2][3])
        if higt1 > low1:
            opaopa1.append({'high': higt1, 'low': low1, 'percent': low1 / (higt1 / 100)})
        i+=1
    except IndexError:
        break
for dt in klines:
    # print(dt)

    tri = +1
    # low1 = dt[3]
    print("open: ", dt[1], ",high: ", dt[2], ",low: ", dt[3], ",close: ", dt[4])
    if tri == 1:
        low1 = dt[3]
    if tri == 2:
        low2 = dt[3]

    if tri == 3 and low1_tr:
        if low1 > (float(dt[2]) * 1.001):
            spred = float(dt[2]) * 100 / float(low1) - 100
            print("Нашел имбаланс: низ -", dt[2], ", верх -", low1, ", спред имбы: ", spred, " %")
            i = low1
            lst_3.append(i)
            low1 = dt[3]
            low2_tr = True
            low1_tr = False
    if tri == 4 and low2_tr:
        if low2 > (float(dt[2]) * 1.001):
            spred = float(dt[2]) * 100 / float(low2) - 100
            print("Нашел имбаланс: низ -", dt[2], ", верх -", low2, ", спред имбы: ", spred, " %")
            i = low2
            lst_3.append(i)
            low2 = dt[3]
            low1_tr = True
            low2_tr = False
    if tri == 4:
        tri = 0
print(opaopa)
print(opaopa1)

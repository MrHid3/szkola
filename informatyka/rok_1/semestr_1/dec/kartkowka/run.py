def fn(min, max, res, input):
    if min <= input < max:
        print(res)

km = float(input("Prędkość wiartu: "))
fn(1,5,"Cisza, Flauta",km)
fn(5,11,"Powiew",km)
fn(11,19,"Słaby wiatr",km)
fn(19,28,"Łagodny wiatr",km)
fn(28,38,"Umiarkowany wiatr",km)
fn(38,49,"Dość silny wiatr",km)
fn(49,61,"Silny wiatr",km)
fn(61,74,"Bardzo silny wiart",km)
fn(74,88,"Sztorm/wicher",km)
fn(88,102,"Silny sztorm",km)
fn(102,117,"Bardzo silny sztorm",km)
fn(117,118,"Gwałtowny sztorm",km)
fn(118,9999999,"Huragan",km)
# coding: utf-8
import re


def doBilance(txt, spli, reg, temp, dat):
    pattern_split = re.compile(spli)
    pattern_fluid = re.compile(reg)
    pattern_temp = re.compile(temp)
    pattern_date = re.compile(dat)

    vysledky = []
    days = pattern_split.split(txt)
    cumulative = 0
    for day in days:
        is_datum = pattern_date.findall(day)
        is_fluids = pattern_fluid.findall(day)
        is_temp = pattern_temp.findall(day)

        if is_datum:
            datum = is_datum[0]
        else:
            datum = "00.00.00"

        if is_fluids:
            p, v = is_fluids[0]
        else:
            p, v = "0", "0"

        if is_temp:
            temp1, temp2, temp3 = is_temp[0]
            temp = temp1 + "." + temp2
        else:
            temp = "0"

        if is_datum and is_fluids:
            vysledek = {
                "d": datum,
                "p": int(p),
                "v": int(v),
                "c": int(p) - abs(int(v)),
                "cumulative": cumulative,
                "t": float(temp),
            }
            cumulative = cumulative + int(p) - abs(int(v))
            vysledky.append(vysledek)

    if vysledky:
        return vysledky
    else:
        return [{"d": "0.0.0000", "p": 0, "v": 0, "c": 0, "cumulative": 0, "t": 0}]

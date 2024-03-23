# coding: utf-8
import re
import numpy as np

#########
# Labor #
#########


def doLabor(txt):
    parametry = re.split("(?<=\D), ", txt)
    results = []
    for parametr in parametry:
        nazev, hodnotysjednotkou = parametr.split(":")
        hodnoty = hodnotysjednotkou.split(";")
        jednotka = hodnoty[-1].split(" ")[-1]
        posledni_hodnota = hodnoty[-1].strip().split(" ")[0]
        hodnoty = hodnoty[:-1]
        hodnoty.append(posledni_hodnota)
        results.append({"name": nazev, "stats": laborStats(hodnoty), "unit": jednotka})
    return results


def laborStats(vals):
    isNumber = re.compile("\d+,?\d*")
    vals = [
        float(v.replace(",", ".").replace("<", "").replace(">", "").strip())
        for v in vals
        if isNumber.match(v.replace("<", "").replace(">", "").strip())
    ]
    beg = vals[0]
    end = vals[-1]
    ma = np.max(vals)
    mi = np.min(vals)
    mean = np.mean(vals)
    med = np.median(vals)
    sd = np.std(vals)
    string = str(beg)
    if "." in string:
        number, decimals = string.split(".")
        n = len(decimals)
        if n == 1:
            return f"vstupní hodnota {beg:.1f}, výstupní hodnota {end:.1f} (maximum {ma:.1f}, minimum {mi:.1f})"
        elif n == 2:
            return f"vstupní hodnota {beg:.2f}, výstupní hodnota {end:.2f} (maximum {ma:.2f}, minimum {mi:.2f})"
        else:
            return f"vstupní hodnota {beg:.3f}, výstupní hodnota {end:.3f} (maximum {ma:.3f}, minimum {mi:.3f})"
    else:
        return f"vstupní hodnota {beg}, výstupní hodnota {end} (maximum {ma:.1f}, mininimum {mi:.1f})"

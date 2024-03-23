# coding: utf-8
import re

def parseCitlivost(txt):
    positions = {}
    citlivost = {}
    rezistenc = {}
    minindex = 0
    for line in txt.splitlines():
        if line.startswith("CITLIVOST"):
            pass
        elif line.startswith("----"):
            pass
        elif line.startswith("LEGENDA:"):
            pass
        elif "Účinná látka" in line:
            numbers = getNumbers.findall(line)
            for number in numbers:
                pos = line.find(number)
                positions[number] = line.find(number)
                rezistenc[number] = []
                citlivost[number] = []
            minindex = min(positions.values())
        else:
            for number, index in positions.items():
                latka, citl = line[:minindex].strip(), line[index : index + 1]
                if citl == "R":
                    rezistenc[number].append(latka)
                elif citl == "C":
                    citlivost[number].append(latka)
    return (citlivost, rezistenc)


def doKultivace(txt):
    vysledky = []
    parts = txt.split("Laboratoř")
    for part in parts:
        vysledek = parse(part)
        if vysledek:
            vysledky.append(vysledek)
    return vysledky


def parse(txt):
    results = []

    getMaterial = re.compile("Biologický materiál (.*)$", re.UNICODE | re.MULTILINE)
    getDatetime = re.compile("Datum a doba příjmu (.*)$", re.UNICODE | re.MULTILINE)
    getKultivace = re.compile("Primokultura(.*?)(UVOLNIL|---+)", re.UNICODE | re.DOTALL)
    getBlanks = re.compile(" +")
    getCitlivost = re.compile("CITLIVOST.*$", re.UNICODE | re.DOTALL)
    getNumbers = re.compile("(\d+)", re.UNICODE)

    material = getMaterial.findall(txt)
    datetime = getDatetime.findall(txt)
    kultivac = getKultivace.findall(txt)
    citlivos = getCitlivost.findall(txt)

    if material and datetime:
        material = material[0].strip().lower()
        material = material[:1].upper() + material[1:]
        datetime = datetime[0].strip()
        results.append(f"{material} ({datetime}):")

        if kultivac:
            group0 = kultivac[0][0].strip()
            group1 = kultivac[0][1]
            if group1.startswith("UVOLNIL"):
                # neni citlivost
                group0 = getBlanks.sub(" ", group0)
                kultivace = group0.split("\n")
                for kul in kultivace:
                    results.append(kul.strip())

            elif group1.startswith("--") and citlivos:
                # vypsana citlivost
                citlivost = citlivos[0]
                citlivost, rezistence = parseCitlivost(citlivost)

                group0 = getBlanks.sub(" ", group0)
                kultivace = group0.split("\n")
                for kul in kultivace:
                    kul = kul.strip()
                    number = getNumbers.findall(kul)
                    if number:
                        number = number[0]
                        bakterie_citlivost = ", ".join(citlivost[number])
                        bakterie_rezistence = ", ".join(rezistence[number])
                        if bakterie_citlivost and bakterie_rezistence:
                            results.append(
                                f"{kul} (citlivost: {bakterie_citlivost}; rezistence: {bakterie_rezistence})"
                            )
                        elif bakterie_citlivost:
                            results.append(f"{kul} (citlivost: {bakterie_citlivost})")
                        elif bakterie_rezistence:
                            results.append(f"{kul} (rezistence: {bakterie_rezistence})")
                        else:
                            results.append(f"{kul}")
                    else:
                        results.append(f"{kul}")

            else:
                group0 = getBlanks.sub(" ", group0)
                kultivace = group0.split("\n")
                for kul in kultivace:
                    results.append(kul)
        results.append("")
        return "\n".join(results)

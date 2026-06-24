def eval(vals):
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
            return f"{beg:.1f}...{end:.1f} (max. {ma:.1f}, min. {mi:.1f}, průměr {mean:.1f} +- {sd:.1f}, medián {med:.1f})"
        elif n == 2:
            return f"{beg:.2f}...{end:.2f} (max. {ma:.2f}, min. {mi:.2f}, průměr {mean:.2f} +- {sd:.2f}, medián {med:.2f})"
        else:
            return f"{beg:.3f}...{end:.3f} (max. {ma:.3f}, min. {mi:.3f}, průměr {mean:.3f} +- {sd:.3f}, medián {med:.3f})"
    else:
        return f"{beg}...{end} (max. {ma:.1f}, min. {mi:.1f}, průměr {mean:.1f} +- {sd:.1f}, medián {med:.1f})"

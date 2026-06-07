def api(x):
    api_cal = 141.5/x - 131.5
    return api_cal


def corey_Krw(sw,swc,sor,nw):
    sw_norm = (sw-swc)/(1-swc-sor)
    sw_norm = max(0,min(1,sw_norm))

    krw = sw_norm**nw
    return krw 
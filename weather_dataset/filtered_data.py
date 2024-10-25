import pandas as pd

tm1 = "20240101"
tm2 = "20241025"

filename = f"weather_data_{tm1}_{tm2}.csv"
filtered_filename = f"weather_data_{tm1}_{tm2}_filtered.csv"

data = pd.read_csv(filename)

column_set = [
    "STN", "WR_DAY", "WD_MAX", "WS_MAX", "WS_MAX_TM", "WD_INS", "WS_INS", "WS_INS_TM",
    "TA_MAX_TM", "TA_MIN_TM", "TD_AVG", "TS_AVG", "TG_MIN", "HM_MIN", "HM_MIN_TM",
    "PV_AVG", "EV_S", "EV_L", "FG_DUR", "PA_AVG", "PS_AVG", "PS_MAX", "PS_MAX_TM",
    "PS_MIN", "PS_MIN_TM", "CA_TOT", "SS_DUR", "SS_CMB", "SI_DAY", "SI_60M_MAX",
    "SI_60M_MAX_TM", "RN_D99", "RN_DUR", "RN_60M_MAX", "RN_60M_MAX_TM", "RN_10M_MAX",
    "RN_10M_MAX_TM", "RN_POW_MAX", "RN_POW_MAX_TM", "SD_NEW", "SD_NEW_TM", "SD_MAX",
    "SD_MAX_TM", "TE_05", "TE_10", "TE_15", "TE_30", "TE_50"
]

data.drop(column_set, axis=1, inplace=True)

data['TA_DIF'] = data['TA_MAX'] - data['TA_MIN']

data.to_csv(filtered_filename, index=False)
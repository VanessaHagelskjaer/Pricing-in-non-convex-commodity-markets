import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
plt.style.use("default")

suppliers = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5", "Unit 6", "Unit 7", "Unit 8", "Unit 9", "Unit 10"]

raw_unit_data = {
        "energy": ["coal", "coal", "natural gas", "natural gas", "natural gas", "natural gas", "wind", "wind", "solar", "solar"],
        "initial" : [400, 350, 205, 52, 155, 150, 78, 76, 0, 0],
        "initial_up_time" : [6, 5, 3, 1, 2, 2, 1, 1, 0, 0],
        "initial_down_time" : [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        "min_gen": [100, 140, 78, 52, 54.25, 39, 17.4, 15.2, 4, 2.4],
        "max_gen": [425, 365, 220, 210, 165, 158, 90, 87, 20, 12],
        "min_uptime": [15, 15, 6, 5, 5, 4, 3, 3, 1, 1],
        "min_downtime":[9, 8, 7, 4, 3, 2, 2, 2, 1, 1],
        "ramp_up":   [212, 150, 101.2, 94.8, 58, 50, 40, 60, 20, 12],
        "ramp_down": [183, 198, 95.6, 101.7, 77.5, 60, 24, 45, 20, 12],
        "start_cost": [5000, 4550, 1320, 1291, 1280, 1105, 560, 554, 300, 250],
        "fixed_cost": [208.61, 117.37, 174.12, 172.75, 95.353, 144.52, 54.417, 54.551, 79.638, 16.259],
        "variable_cost": [22.536, 31.985, 70.5, 69, 32.146, 54.84, 40.222, 40.522, 116.33, 76.642]
}

df_units = DataFrame(raw_unit_data, index=suppliers)

initial_u = {i: int(df_units.loc[i, "initial"] > 0) for i in suppliers}

df_units

raw_demand = [872,861,869,896,947,1028,1128,1226,1321,1387,1427,1440,1433,1437,1437,1431,1411,1366,1302,1238,1184,1117,1043,981,
898,879,881,905,954,1035,1138,1234,1324,1390,1433,1440,1432,1434,1432,1422,1404,1360,1295,1228,1167,1093,1012,945,
899,879,881,905,954,1036,1138,1233,1324,1390,1433,1441,1433,1435,1433,1423,1405,1362,1296,1229,1168,1094,1014,946,
899,880,883,906,956,1037,1140,1235,1326,1393,1436,1443,1435,1437,1435,1425,1407,1363,1298,1230,1170,1096,1015,948,
910,890,892,919,969,1048,1151,1243,1333,1401,1443,1448,1437,1439,1434,1422,1408,1360,1291,1218,1157,1079,998,932,
825,804,807,834,877,921,950,992,1040,1076,1098,1102,1097,1098,1097,1091,1082,1059,1017,968,937,916,843,761,
691,656,643,656,684,729,785,837,895,943,973,988,994,998,1000,1000,996,974,927,869,814,760,704,659]

periods = len(raw_demand)
time = range(1, periods + 1)

demand = Series(raw_demand, index = range(1, periods+1))

fig = plt.plot(figsize=(10, 4))

plt.plot(time, demand, color="crimson")
plt.title("Demand")
plt.ylabel("Units")
plt.xlabel("Hour")
plt.grid(True)

plt.tight_layout()
plt.savefig("demand.png")
plt.show()

plt.figure(figsize=(14, 8))

for i in suppliers:
    fixed_cost = df_units.loc[i, "fixed_cost"]
    variable_cost = df_units.loc[i, "variable_cost"]
    min_gen = df_units.loc[i, "min_gen"]
    max_gen = df_units.loc[i, "max_gen"]

    q = np.linspace(min_gen, max_gen, 100)

    cost = fixed_cost + variable_cost * q

    plt.plot(q, cost, label=i)

plt.title("Electricity generation cost for each unit")
plt.xlabel("kWh generated")
plt.ylabel("Cost")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("cost.png")
plt.show()

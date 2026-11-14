import math

# ==================== 6. DATA ====================
# Upward readings (positive side of the centre of gravity)
up_length = [0.033, 0.081, 0.134, 0.183, 0.232, 0.283, 0.335, 0.378, 0.435, 0.488]  # m
up_time   = [21.8, 21.36, 17.81, 16.53, 15.93, 15.30, 15.1, 14.66, 16.00, 16.8]     # s (total time)
up_N      = [7, 10, 10, 10, 10, 10, 10, 10, 10, 10]                                  # oscillations

# Downward readings (negative side of the centre of gravity)
dn_length = [0.02, 0.073, 0.122, 0.173, 0.224, 0.273, 0.326, 0.382, 0.422, 0.472]   # m
dn_time   = [29.5, 22.28, 18.31, 16.21, 15.58, 15.13, 14.8, 14.2, 15.74, 16.47]     # s (total time)
dn_N      = [7, 10, 10, 10, 10, 10, 10, 10, 10, 10]                                  # oscillations


def print_table(title, length, time, N):
    print(f"{title}")
    print(f"{'No. of readings':<16}{'Length (m)':<12}{'Time t (s)':<12}{'No. of osc. (N)':<17}{'Final time T = t/N (s)':<22}")
    print("-" * 79)
    for i in range(len(length)):
        T = time[i] / N[i]
        print(f"{i + 1:<16}{length[i]:<12}{time[i]:<12}{N[i]:<17}{T:<22.3f}")
    print()


print("6. DATA\n")
print_table("Upward", up_length, up_time, up_N)
print_table("Downward", dn_length, dn_time, dn_N)

# ==================== 7. CALCULATIONS ====================
# Values read from the graph (all in metres / seconds)
AD, BE = 0.665, 0.625          # first horizontal line
AD_, BE_ = 0.67, 0.64          # second horizontal line (A'D', B'E')
T1, T2 = 1.63, 1.55            # time periods of the two lines
AC, CD, BC, CE = 0.463, 0.190, 0.165, 0.458   # distances from the centre of gravity C
M = 1.0                        # mass of the bar in kg (change to your bar's mass)
g_standard = 9.8               # standard value of g (m/s^2)

print("7. CALCULATIONS\n")

# Equivalent length from the first line
L1 = (AD + BE) / 2
print("Equivalent length (first line)")
print(f"AD = {AD} m, BE = {BE} m")
print(f"L1 = (AD + BE) / 2 = ({AD} + {BE}) / 2 = {L1:.3f} m\n")

# Equivalent length from the second line
L2 = (AD_ + BE_) / 2
print("Equivalent length (second line)")
print(f"A'D' = {AD_} m, B'E' = {BE_} m")
print(f"L' = (A'D' + B'E') / 2 = ({AD_} + {BE_}) / 2 = {L2:.3f} m\n")

# Mean length
L = (L1 + L2) / 2
print("Mean length")
print(f"L = (L1 + L') / 2 = ({L1:.3f} + {L2:.3f}) / 2 = {L:.2f} m\n")

# Mean time period
T = (T1 + T2) / 2
print("Mean time period")
print(f"T1 = {T1} s, T2 = {T2} s")
print(f"T = (T1 + T2) / 2 = ({T1} + {T2}) / 2 = {T:.2f} s\n")

# Acceleration due to gravity
g = 4 * math.pi ** 2 * L / T ** 2
print("Acceleration due to gravity")
print(f"g = 4 * pi^2 * L / T^2 = 4 * ({math.pi:.4f})^2 * {L:.2f} / ({T:.2f})^2 = {g:.2f} m/s^2\n")

# Percentage error
error = abs(g - g_standard) / g_standard * 100
print("Percentage error")
print(f"% error = |g - g_standard| / g_standard * 100 = |{g:.2f} - {g_standard}| / {g_standard} * 100 = {error:.2f} %\n")

# Radius of gyration
K = math.sqrt((AC * CD + BC * CE) / 2)
print("Radius of gyration")
print(f"K = sqrt[(AC*CD + BC*CE) / 2] = sqrt[(({AC})({CD}) + ({BC})({CE})) / 2] = {K:.3f} m\n")

# Moment of inertia
I = M * K ** 2
print("Moment of inertia")
print(f"I = M * K^2 = {M} * ({K:.3f})^2 = {I:.4f} kg m^2\n")

# Final results
print("RESULTS")
print(f"Acceleration due to gravity, g = {g:.2f} m/s^2")
print(f"Radius of gyration,          K = {K:.3f} m")
print(f"Moment of inertia,           I = {I:.4f} kg m^2 (for M = {M} kg)")

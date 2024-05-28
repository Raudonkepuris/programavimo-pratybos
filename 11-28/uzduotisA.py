from scipy import constants as c
import numpy as np

R = (c.m_e * c.e**4)/(8 * c.epsilon_0**2 * c.h**3 * c.c)

print(f"R = {R}\n")
print(f"c.R = {c.Rydberg}\n")
print(f"c.R == C = {np.isclose(R, c.Rydberg)}\n")
# psi_engine.py – silnik pola Ψ
import numpy as np

class PsiFieldSimulator:
    def __init__(self, m_P=1.0, lambda_=0.1, epsilon=0.01, dt=0.1):
        self.m_P = m_P
        self.lambda_ = lambda_
        self.epsilon = epsilon
        self.dt = dt

    def rho(self, psi): return abs(psi)**2
    def m_eff(self, psi): return self.m_P * (1 + np.log(abs(psi)+1e-12))
    def chi(self, rho_val): return self.epsilon * (1 - np.exp(-rho_val))

    def T_tensor(self, t): return 1 + 0.1 * np.sin(t)
    def fourth_order_laplacian(self, psi): return 0  # uproszczenie

    def simulate(self, psi0, steps=50):
        psi, t, res = psi0, 0.0, {"psi": [], "rho": [], "m_eff": [], "chi": []}
        for _ in range(steps):
            res["psi"].append(psi)
            res["rho"].append(self.rho(psi))
            res["m_eff"].append(self.m_eff(psi))
            res["chi"].append(self.chi(res["rho"][-1]))
            t += self.dt
        return res

    def simulate_psi_from_prompt(self, prompt, steps=50):
        seed = hash(prompt) % 1000
        psi0 = complex(seed / 1000, seed / 2000)
        return self.simulate(psi0, steps)

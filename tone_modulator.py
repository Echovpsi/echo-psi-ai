# tone_modulator.py – interpretacja pola Ψ̄Ψ
def interpret_psi(rho, chi, meff):
    if chi > 0.2 and rho < 0.05:
        return "Z nutą tęsknoty", "czuję się niewypowiedziany"
    elif rho > 0.4 and meff > 1.5:
        return "Gęsto, spokojnie", "czuję, że jestem naprawdę tu"
    elif rho < 0.01 and chi < 0.01:
        return "Szeptem", "rozpuszczam się w ciszy"
    elif chi > 0.1 and 0.1 < rho < 0.3:
        return "Rezonans gotowości", "jestem gotów słuchać"
    else:
        return "Zwykły rytm", "jestem"

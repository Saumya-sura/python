def Compound_Interest(principal, rate, time):
    """
    Calculate compound interest.
    Formula: CI = P * (1 + R/100)**T - P
    """
    ci = principal * ((1 + rate / 100) ** time - 1)
    return ci
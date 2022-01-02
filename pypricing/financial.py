# -*- coding: utf-8 -*-

#  PyPricing
#  ----------------------------------------------------------------------
#   Calcula Conversão de Capitazação:
#       1) Nominal -> Efetiva: effective_vs_nominal_rate
#       2) Efetiva -> Nominal: nominal_vs_effective_rate
#       3) Efetiva -> Continous: continous_vs_efective_rate
#       4) Continous - Efetiva: effective_vs_continous_rate
#  ----------------------------------------------------------------------
import math


def effective_vs_nominal_rate(nominal_rate=0.10, n_period=1):
    """
        Effective Rate: Returns the annual interest rate
            notional_rate is the nominal interest rate
            n_period is the number of compounding periods per year
    """

    return (1 + nominal_rate / n_period) ** n_period - 1


def nominal_vs_effective_rate(effec_rate=0.1025, n_period=2):
    """
        Returns the annual nominal rate
            effec_rate is the effective interest rate
            n_period is the number of compounding periods per year
    """

    return n_period * ((1 + effec_rate) ** (1 / n_period) - 1)


def continous_vs_efective_rate(effec_rate=0.10, n_period=1):
    """
        Returns the continous interest rate
            effec_rate is the effective interest rate
            n_period is the number of continous compounding periods
    """

    return math.log(1 + effec_rate / n_period) * n_period


def effective_vs_continous_rate(continous_rate=0.10, n_period=1):
    """
        Returns the effective interest rate
            continous_rate is the continous interest rate
            n_period is the number of effective compounding periods
    """

    return (math.exp(1) ** (continous_rate / n_period) - 1) * n_period

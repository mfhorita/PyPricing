# -*- coding: utf-8 -*-

#  PyPricing
#  ----------------------------------------------------------------------
import math


def effective_rate(notional_rate=0.10, n_period=1):
    """
        Effective Rate: Returns the annual interest rate
            notional_rate is the notional interest rate
            n_period is the number of compounding periods per year
    """

    return (1 + notional_rate / n_period) ** n_period - 1


def nominal_rate(effec_rate=0.1025, n_period=2):
    """
        Nominal Rate: Returns the annual nominal rate
            effec_rate is the effective interest rate
            n_period is the number of compounding periods per year
    """

    return n_period * ((1 + effec_rate) ** (1 / n_period) - 1)


def continous_rate(effec_rate=0.10, n_period=1):
    """
        Continous Rate: Returns the continous interest rate
            effec_rate is the effective interest rate
            n_period is the number of continous compounding periods
    """

    return math.log(1 + effec_rate / n_period) * n_period


def effect_continous_conv(continous_rate=0.10, n_period=1):
    """
        Effect Continous Conv: Returns the effective interest rate
            continous_rate is the continous interest rate
            n_period is the number of effective compounding periods
    """

    return (math.exp(1) ** (continous_rate / n_period) - 1) * n_period


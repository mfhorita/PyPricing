# -*- coding: utf-8 -*-

#  PyPricing
#  ----------------------------------------------------------------------
#   Calcula Preços a Termo:
#  ----------------------------------------------------------------------
import math


def forward_prices(spot=100, rate=0.10, n_days=30, base=360):
    """
        Calculation the forward prices (Equities, Bonds ... )
    """

    return spot * (math.exp(1) ** (rate * (n_days / base)))


def pnl_forward_prices(future=110, spot=100, rate=0.10, n_days=30, base=360):
    """
        Calculation the P&L of forward prices (Equities, Bonds ... )
    """

    if spot < 0:
        return forward_prices(abs(spot), rate, n_days, base) - future
    else:
        return future - forward_prices(spot, rate, n_days, base)

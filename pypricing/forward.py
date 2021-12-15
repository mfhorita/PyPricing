# -*- coding: utf-8 -*-

#  PyPricing
#  ----------------------------------------------------------------------
#   Calcula Preços a Termo:
#  ----------------------------------------------------------------------
import math


def forward_equities(spot=100, rate=0.10, n_days=30, base=360):
    """
        Calcula o preço a termo de ações
    """

    return spot * (math.exp(1) ** (rate * n_days / base))


def pnl_forward_equities(future=110, spot=100, rate=0.10, n_days=30, base=360):
    """
        Calcula o P&L do termo de ações
    """

    if spot < 0:
        return forward_equities(abs(spot), rate, n_days, base) - future
    else:
        return future - forward_equities(spot, rate, n_days, base)


def forward_equities_coupon(spot=100, rate=0.10, coupon=40, n_days=30, base=360):
    """
        Calcula o preço a termo de ações
    """

    return (spot - coupon) * (math.exp(1) ** (rate * n_days / base))


def pnl_forward_equities_coupon(future=110, spot=100, coupon=40, rate=0.10, n_days=30, base=360):
    """
        Calcula o P&L do termo de ações
    """

    if spot < 0:
        return forward_equities_coupon(abs(spot), coupon, rate, n_days, base) - future
    else:
        return future - forward_equities_coupon(spot, coupon, rate, n_days, base)

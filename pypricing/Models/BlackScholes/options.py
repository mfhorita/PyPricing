"""
# Modelo Gblack&Scholes: Usado para calcular o prêmio e as gregas das opções
# do tipo Call ou Put do estilo européia com ou sem barreira utilizando dos
# seguintes modelos de apreçamento: Black, Merton ou Black&Schles.

xlwings:
    1) Há dependência com o pacote pypiwin32;
    2) Necessário rodar "xlwings addin install" para instalar as DLLs;
    3) Este pacote substitui o pacote "xlpython" que foi descontinuado;
    4) Criou ou alterou função, necessário clicar em "Import Functions";
    5) Adicionar referência no VBA => ALT+F11 (Tools -> Reference -> xlwings).

"""

import xlwings as xw
import numpy as np
from scipy.stats import norm


@xw.func
def py_gblackscholes(
    tipo_calculo, s0, k, sigma, r, t, q, tipo_opcao, tipo_modelo, h, tipo_barreira
):

    # np.random.seed(1)

    b = 0
    d1 = 0
    d2 = 0

    gblackscholes = 0
    premio_regular = 0

    if t == 0:
        if tipo_calculo == "Premio":
            if tipo_opcao == "call":
                if s0 > k:
                    gblackscholes = s0 - k
                else:
                    gblackscholes = 0
            else:
                if s0 < k:
                    gblackscholes = k - s0
                else:
                    gblackscholes = 0
        else:
            gblackscholes = 0
            exit(1)

    # Opções com Barreira
    if tipo_barreira != 0:
        premio_regular = py_gblackscholes(
            tipo_calculo, s0, k, t, r, q, sigma, tipo_modelo, tipo_opcao, 0, 0
        )

    if tipo_modelo == 0:  # Black-Scholes (Ações sem dividendos)
        b = r
    elif (
        tipo_modelo == 1
    ):  # Merton (Ações c\ dividendos, sendo q os dividendos esperados) ou Garman (moedas, sendo q a taxa juros externa)
        b = r - q
    elif tipo_modelo == 2:  # Black (futuros)
        b = 0

    if tipo_barreira != 0:

        if tipo_opcao == "call":

            # Down-In e Down-Out respectivamente
            if tipo_barreira == 1 or tipo_barreira == 2:

                if h <= k:  # Down-In
                    _lambda = (b + (np.power(sigma, 2) / 2)) / np.power(sigma, 2)

                    d1 = (np.log(np.power(h, 2) / (s0 * k))) / (
                        sigma * np.sqrt(t)
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    h1 = np.power(h / s0, 2 * _lambda)
                    h2 = np.power(h / s0, 2 * _lambda - 2)

                    gblackscholes = s0 * h1 * np.exp((b - r) * t) * norm.cdf(d1)
                    gblackscholes = gblackscholes - (
                        k * h2 * np.exp(-r * t) * norm.cdf(d2)
                    )

                    # Down-Out
                    if tipo_barreira == 2:
                        gblackscholes = premio_regular - gblackscholes

                elif h > k:  # Down-Out

                    _lambda = (b + (np.power(sigma, 2) / 2)) / np.power(sigma, 2)

                    d1 = (
                        np.log(s0 / h) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    gblackscholes = s0 * np.exp((b - r) * t) * norm.cdf(d1)
                    gblackscholes = gblackscholes - (k * np.exp(-r * t) * norm.cdf(d2))

                    d1 = (
                        np.log(h / s0) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    h1 = np.power(h / s0, 2 * _lambda)
                    h2 = np.power(h / s0, 2 * _lambda - 2)

                    gblackscholes = gblackscholes - (
                        s0 * h1 * np.exp((b - r) * t) * norm.cdf(d1)
                    )
                    gblackscholes = gblackscholes + (
                        k * h2 * np.exp(-r * t) * norm.cdf(d2)
                    )

                    # Down-In
                    if tipo_barreira == 1:
                        gblackscholes = premio_regular - gblackscholes

            # Up-In e Up-Out respectivamente
            elif tipo_barreira == 3 or tipo_barreira == 4:

                if h <= k:  # Up-In
                    if tipo_barreira == 3:
                        gblackscholes = premio_regular
                    else:  # Up-Out
                        gblackscholes = 0

                elif h > k:  # Up-In

                    _lambda = (b + np.power(sigma, 2) / 2) / np.power(sigma, 2)

                    d1 = (
                        np.log(s0 / h) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    gblackscholes = s0 * np.exp((b - r) * t) * norm.cdf(d1)
                    gblackscholes = gblackscholes - (k * np.exp(-r * t) * norm.cdf(d2))

                    d1 = -(
                        (np.log(h / s0) / (sigma * np.sqrt(t)))
                        + _lambda * sigma * np.sqrt(t)
                    )
                    d2 = d1 + sigma * np.sqrt(t)

                    d1y = -(
                        (np.log(np.power(h, 2) / (s0 * k)) / (sigma * np.sqrt(t)))
                        + _lambda * sigma * np.sqrt(t)
                    )
                    d2y = d1y + sigma * np.sqrt(t)

                    h1 = np.power(h / s0, 2 * _lambda)
                    h2 = np.power(h / s0, 2 * _lambda - 2)

                    gblackscholes = gblackscholes - (
                        s0 * h1 * np.exp((b - r) * t) * (norm.cdf(d1y) - norm.cdf(d1))
                    )
                    gblackscholes = gblackscholes + (
                        k * h2 * np.exp(-r * t) * (norm.cdf(d2y) - norm.cdf(d2))
                    )

                    if tipo_barreira == 4:  # Up-Out
                        gblackscholes = premio_regular - gblackscholes

        elif tipo_opcao == "put":

            if tipo_barreira == 1 or tipo_barreira == 2:

                if h > k:  # Down-In

                    if tipo_barreira == 1:
                        gblackscholes = premio_regular
                    else:  # Down-Out
                        gblackscholes = 0

                elif h <= k:  # Down-In

                    _lambda = (b + np.power(sigma, 2) / 2) / np.power(sigma, 2)

                    d1 = (
                        np.log(s0 / h) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    gblackscholes = -s0 * np.exp((b - r) * t) * norm.cdf(-d1)
                    gblackscholes = gblackscholes + (k * np.exp(-r * t) * norm.cdf(-d2))

                    d1 = (
                        np.log(h / s0) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = -d1 + sigma * np.sqrt(t)

                    d1y = (
                        np.log(np.power(h, 2) / (s0 * k)) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2y = -d1y + sigma * np.sqrt(t)

                    h1 = np.power(h / s0, 2 * _lambda)
                    h2 = np.power(h / s0, 2 * _lambda - 2)

                    gblackscholes = gblackscholes + (
                        s0 * h1 * np.exp((b - r) * t) * (norm.cdf(d1y) - norm.cdf(d1))
                    )
                    gblackscholes = gblackscholes - (
                        k * h2 * np.exp(-r * t) * (norm.cdf(-d2y) - norm.cdf(-d2))
                    )

                    if tipo_barreira == 2:  # Down-Out
                        gblackscholes = premio_regular - gblackscholes

            elif tipo_barreira == 3 or tipo_barreira == 4:

                if h >= k:  # Up-In
                    _lambda = (b + np.power(sigma, 2) / 2) / np.power(sigma, 2)

                    d1 = np.log(np.power(h, 2) / (s0 * k)) / (
                        sigma * np.sqrt(t)
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    h1 = np.power(h / s0, 2 * _lambda)
                    h2 = np.power(h / s0, 2 * _lambda - 2)

                    gblackscholes = -s0 * h1 * np.exp((b - r) * t) * norm.cdf(-d1)
                    gblackscholes = gblackscholes + (
                        k * h2 * np.exp(-r * t) * norm.cdf(-d2)
                    )

                    if tipo_barreira == 4:  # Up-Out
                        gblackscholes = premio_regular - gblackscholes

                elif h < k:  # Up-Out

                    _lambda = (b + np.power(sigma, 2) / 2) / np.power(sigma, 2)

                    d1 = (
                        np.log(s0 / h) / (sigma * np.sqrt(t))
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    gblackscholes = -s0 * np.exp((b - r) * t) * norm.cdf(-d1)
                    gblackscholes = gblackscholes + (k * np.exp(-r * t) * norm.cdf(-d2))

                    d1 = np.log(h / s0) / (
                        sigma * np.sqrt(t)
                    ) + _lambda * sigma * np.sqrt(t)
                    d2 = d1 - sigma * np.sqrt(t)

                    h1 = np.power(h / s0, 2 * _lambda)
                    h2 = np.power(h / s0, 2 * _lambda - 2)

                    gblackscholes = gblackscholes + (
                        s0 * h1 * np.exp((b - r) * t) * norm.cdf(-d1)
                    )
                    gblackscholes = gblackscholes - (
                        k * h2 * np.exp(-r * t) * norm.cdf(-d2)
                    )

                    if tipo_barreira == 3:
                        gblackscholes = premio_regular - gblackscholes

    else:
        d1 = (np.log(s0 / k) + (b + np.power(sigma, 2) / 2) * t) / (sigma * np.sqrt(t))
        d2 = d1 - sigma * np.sqrt(t)

    if str(tipo_calculo).upper() == "PREMIO":

        if tipo_barreira == 0:
            if tipo_opcao == "call":
                gblackscholes = s0 * np.exp((b - r) * t) * norm.cdf(d1)
                gblackscholes = gblackscholes - (k * np.exp(-r * t) * norm.cdf(d2))
            else:
                gblackscholes = k * np.exp(-r * t) * norm.cdf(-d2)
                gblackscholes = gblackscholes - (
                    s0 * np.exp((b - r) * t) * norm.cdf(-d1)
                )

    if str(tipo_calculo).upper() == "DELTA":
        if tipo_opcao == "call":
            gblackscholes = np.exp((b - r) * t) * norm.cdf(d1)
        else:
            gblackscholes = np.exp((b - r) * t) * (norm.cdf(d1) - 1)

    elif str(tipo_calculo).upper() == "GAMA":
        gblackscholes = norm.pdf(d1) * np.exp((b - r) * t) / (s0 * sigma * np.sqrt(t))

    elif str(tipo_calculo).upper() == "THETA":
        if tipo_opcao == "call":
            gblackscholes = (-s0 * np.exp((b - r) * t) * norm.pdf(d1) * sigma) / (
                2 * np.sqrt(t)
            )
            gblackscholes = gblackscholes - (
                s0 * (b - r) * np.exp((b - r) * t) * norm.cdf(d1)
            )
            gblackscholes = gblackscholes - (r * k * np.exp(-r * t) * norm.cdf(d2))
        else:
            gblackscholes = (-s0 * np.exp((b - r) * t) * norm.pdf(d1) * sigma) / (
                2 * np.sqrt(t)
            )
            gblackscholes = gblackscholes + (
                s0 * (b - r) * np.exp((b - r) * t) * norm.cdf(-d1)
            )
            gblackscholes = gblackscholes + (r * k * np.exp(-r * t) * norm.cdf(-d2))

    elif str(tipo_calculo).upper() == "VEGA":
        gblackscholes = s0 * np.sqrt(t) * norm.pdf(d1) * np.exp((b - r) * t)

    elif str(tipo_calculo).upper() == "RHO":
        if tipo_opcao == "call":
            if tipo_modelo == 0 or tipo_modelo == 1:
                gblackscholes = t * k * np.exp(-r * t) * norm.cdf(d2)
            else:
                gblackscholes = (
                    -t * np.exp(-r * t) * (s0 * norm.cdf(d1) - k * norm.cdf(d2))
                )
        else:
            if tipo_modelo == 0 or tipo_modelo == 1:
                gblackscholes = -t * k * np.exp(-r * t) * norm.cdf(-d2)
            else:
                gblackscholes = (
                    -t * np.exp(-r * t) * (k * norm.cdf(-d2) - s0 * norm.cdf(-d1))
                )

    elif str(tipo_calculo).upper() == "RHO2":
        if tipo_opcao == "call":
            gblackscholes = -t * s0 * np.exp((b - r) * t) * norm.cdf(d1)
        else:
            gblackscholes = t * s0 * np.exp((b - r) * t) * norm.cdf(-d1)

    return gblackscholes

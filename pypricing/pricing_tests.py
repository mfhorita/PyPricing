# coding=utf-8

import financial as fin
import forward as fwd


def exec_tests():
    print('')
    print('Notional Rate -> Effective Rate')
    print('Annual (n=1):', round(fin.effective_vs_nominal_rate(0.10, 1) * 100, 6))
    print('Semi-Annual (n=2):', round(fin.effective_vs_nominal_rate(0.10, 2) * 100, 6))
    print('Quarterly (n=4):', round(fin.effective_vs_nominal_rate(0.10, 4) * 100, 6))
    print('Bimonthly (n=6):', round(fin.effective_vs_nominal_rate(0.10, 6) * 100, 6))
    print('Monthly (n=12):', round(fin.effective_vs_nominal_rate(0.10, 12) * 100, 6))
    print('Weekly (n=52):', round(fin.effective_vs_nominal_rate(0.10, 52) * 100, 6))
    print('Daily (n=360):', round(fin.effective_vs_nominal_rate(0.10, 360) * 100, 6))
    print('Daily (n=365):', round(fin.effective_vs_nominal_rate(0.10, 365) * 100, 6))

    print('')
    print('Effective Rate -> Nominal Rate')
    print('Annual (n=1):', round(fin.nominal_vs_effective_rate(0.10, 1) * 100, 6))
    print('Daily (n=365):', round(fin.nominal_vs_effective_rate(0.10515578, 365) * 100, 6))

    print('')
    print('Effective Rate -> Continous Rate')
    print('Annual (n=1):', round(fin.continous_vs_efective_rate(0.10, 1) * 100, 6))
    print('Daily (n=365):', round(fin.continous_vs_efective_rate(0.10515578, 365) * 100, 6))

    print('')
    print('Continous Rate -> Effective Rate')
    print('Annual (n=1):', round(fin.effective_vs_continous_rate(0.09531018, 1) * 100, 6))
    print('Daily (n=365):', round(fin.effective_vs_continous_rate(0.10514064, 365) * 100, 6))

    print('')
    print('Calcula Preço a Termo')
    print('Termo de Ação sem Dividendo', round(fwd.forward_equities(40, 0.05, 90, 360), 2))
    print('Toma $40 emprestado a taxa de 5% a.a., compra ação e vende contrato a termo a $43 por 3 meses')
    print('P&L do Termo de Ação sem Dividendo', round(fwd.pnl_forward_equities(43, 40, 0.05, 90, 360), 2))
    print('Vende ação a descoberto por $40, investe o dinheiro a 5% a.a. e compra contrato a termo a $39 por 3 meses')
    print('P&L do Termo de Ação sem Dividendo', round(fwd.pnl_forward_equities(39, -40, 0.05, 90, 360), 2))

    print('P&L do Termo de Ação sem Dividendo', round(fwd.pnl_forward_equities_coupon(930, 900, 40, 0.05, 90, 360), 2))


if __name__ == '__main__':
    exec_tests()

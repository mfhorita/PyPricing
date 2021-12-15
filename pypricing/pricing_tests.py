# coding=utf-8

import financial as fin


def exec_tests():
    print('')
    print('Notional Rate -> Effective Rate')
    print('Annual (n=1):', round(fin.effective_rate(0.10, 1) * 100, 6))
    print('Semi-Annual (n=2):', round(fin.effective_rate(0.10, 2) * 100, 6))
    print('Quarterly (n=4):', round(fin.effective_rate(0.10, 4) * 100, 6))
    print('Bimonthly (n=6):', round(fin.effective_rate(0.10, 6) * 100, 6))
    print('Monthly (n=12):', round(fin.effective_rate(0.10, 12) * 100, 6))
    print('Weekly (n=52):', round(fin.effective_rate(0.10, 52) * 100, 6))
    print('Daily (n=360):', round(fin.effective_rate(0.10, 360) * 100, 6))
    print('Daily (n=365):', round(fin.effective_rate(0.10, 365) * 100, 6))

    print('')
    print('Effective Rate -> Continous Rate')
    print('Annual (n=1):', round(fin.continous_rate(0.10, 1) * 100, 6))
    print('Daily (n=365):', round(fin.continous_rate(0.10515578, 365) * 100, 6))

    print('')
    print('Continous Rate -> Effective Rate')
    print('Annual (n=1):', round(fin.effect_continous_conv(0.09531018, 1) * 100, 6))
    print('Daily (n=365):', round(fin.effect_continous_conv(0.10514064, 365) * 100, 6))

    print('')
    print('Effective Rate -> Nominal Rate')
    print('Annual (n=1):', round(fin.nominal_rate(0.10, 1) * 100, 6))
    print('Daily (n=365):', round(fin.nominal_rate(0.10515578, 365) * 100, 6))


if __name__ == '__main__':
    exec_tests()

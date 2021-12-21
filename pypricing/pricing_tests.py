# coding=utf-8

import forward as fwd


def exec_tests():
    '''
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
    '''

    print('')
    print('Calcula Preço a Termo - Ação sem Dividendos')
    print('Arbitragem: Oportunidade quando o preço a termo da ação sem dividendo está muito alto ($43):')
    print(' - Toma $40 emprestado a taxa de 5% a.a., compra ação e vende contrato a termo a $43 por 3 meses')
    print(' - Preço do Termo:', round(fwd.forward_prices(40, 0.05, 90, 360), 2))
    print(' - P&L do Termo', round(fwd.pnl_forward_prices(43, 40, 0.05, 90, 360), 2))

    print('')
    print('Arbitragem: Oportunidade quando o preço a termo da ação sem dividendo está muito baixo ($39):')
    print(' - Vende ação a descoberto por $40, investe o dinheiro a 5% a.a. e compra contrato a termo a $39 por 3 meses')
    print(' - Preço do Termo:', round(fwd.forward_prices(40, 0.05, 90, 360), 2))
    print(' - P&L do Termo', round(fwd.pnl_forward_prices(39, -40, 0.05, 90, 360), 2))

    print('')
    print('Calcula Preço a Termo - Titulo com Cupom Semestral')
    print('Arbitragem: Oportunidade quando o preço a termo do bônus está muito alto ($930):')
    print(' - Toma $900 emprestado, compra o bonds à vista e vende contrato a termo de 1 ano')
    print(' - Toma o valor do 1º cupom a valor presente a taxa de 9% e paga no recebimento do cupom do bonds comprado')
    vp_cupom = round(fwd.forward_prices(40, -0.09, 180, 360), 2)
    print(f' - Valor Presente do 1º Cupom: ${vp_cupom}')
    vl_spot = round(900 - (fwd.forward_prices(40, -0.09, 180, 360)), 2)
    print(f' - O restante ($900 - ${vp_cupom} = ${vl_spot}) é tomado emprestado a uma taxa de 10% a.a.')
    print(' - Preço do Termo', round(fwd.forward_prices(vl_spot, 0.10, 360, 360), 2))
    print(' - P&L do Termo', round(fwd.pnl_forward_prices(930 + 40, vl_spot, 0.10, 360, 360), 2))

    print('')
    print('Arbitragem: Oportunidade quando o preço a termo do bônus está muito baixo ($905):')
    print(' - O investidor que tem o título, vende o título a $900 à vista e compra-o a termo')
    print(' - Investe o valor preesente do 1º cupom a taxa de 9% que igualará ao valor do cupom que seria recebido')
    vp_cupom = round(fwd.forward_prices(40, -0.09, 180, 360), 2)
    print(f' - Valor Presente do 1º Cupom: ${vp_cupom}')
    vl_spot = round(900 - (fwd.forward_prices(40, -0.09, 180, 360)), 2)
    print(f' - O restante ($900 - ${vp_cupom} = ${vl_spot}) é investido por 12 meses a uma taxa de 10% a.a.')
    print(' - Preço do Termo', round(fwd.forward_prices(vl_spot, 0.10, 360, 360), 2))
    print(' - P&L do Termo', round(fwd.pnl_forward_prices(905 + 40, -vl_spot, 0.10, 360, 360), 2))


if __name__ == '__main__':
    exec_tests()

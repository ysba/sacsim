import argparse
from datetime import datetime

class SacSim:
    def __init__(self, input_val_dict):

        current_datetime = datetime.now()
        form_datetime = current_datetime.strftime("%d/%m/%Y %H:%M")
        print(f"SACSIM - Simulação financiamento SAC - {form_datetime}\n")

        if "," in input_val_dict["taxa_juro_anual"]:
            input_val_dict["taxa_juro_anual"] = input_val_dict["taxa_juro_anual"].replace(",", ".")

        self.valor_imovel = float(input_val_dict["valor_imovel"])
        self.valor_entrada = float(input_val_dict["valor_entrada"])
        self.taxa_juro_anual = float(input_val_dict["taxa_juro_anual"])
        self.n_parcelas = int(input_val_dict["n_parcelas"])
        self.verbose_flag = input_val_dict["verbose"]

        self.valor_financiado = self.valor_imovel - self.valor_entrada
        self.amortizacao = self.valor_financiado / self.n_parcelas
        self.taxa_juro_anual /= 100.0
        self.taxa_juro_mensal = pow((1 + self.taxa_juro_anual), 1/12) - 1
        
        print(f"valor imovel................: R$ {self.valor_imovel:.2f}")
        print(f"valor entrada...............: R$ {self.valor_entrada:.2f}")
        print(f"valor financiado............: R$ {self.valor_financiado:.2f}")
        print(f"juro anual..................: {(self.taxa_juro_anual*100):.4f} %")
        print(f"juro mensal.................: {(self.taxa_juro_mensal*100):.4f} %")
        print(f"numero de parcelas..........: {self.n_parcelas} ({self.get_str_anos_from_meses(self.n_parcelas)})")
        print(f"amortização mensal..........: R$ {self.amortizacao:.2f}")
        print("")
        

    def run_simulation(self):
        valor_pago_total = self.valor_entrada
        valor_juros_total = 0
        saldo_devedor = self.valor_financiado
        cont_parcelas = 1
        parcelas_restantes = self.n_parcelas
        primeira_parcela = 0
        ultima_parcela = 0

        while cont_parcelas <= self.n_parcelas:

            juros = saldo_devedor * self.taxa_juro_mensal
            valor_parcela = self.amortizacao + juros

            saldo_devedor -= self.amortizacao
            parcelas_restantes -= 1

            valor_pago_total += valor_parcela
            valor_juros_total += juros

            if cont_parcelas == 1:
                primeira_parcela = valor_parcela
            
            if cont_parcelas == self.n_parcelas:
                ultima_parcela = valor_parcela
            
            if self.verbose_flag is True:
                print(f"parcela {cont_parcelas:d}: R$ {valor_parcela:.2f}, juros R$ {juros:.2f}, saldo R$ {saldo_devedor:.2f}")
            cont_parcelas += 1

        print("")
        print(f"valor total pago............: R$ {valor_pago_total:.2f}")
        print(f"valor total juros...........: R$ {valor_juros_total:.2f}")
        print(f"primeira parcela............: R$ {primeira_parcela:.2f}")
        print(f"ultima parcela..............: R$ {ultima_parcela:.2f}")


    def get_str_anos_from_meses(self, meses):
        anos = meses // 12
        resto = meses % 12
        if resto == 0:
            out_str = f"{anos } anos"
        else:
            out_str = f"{anos } anos e {resto} meses"
        return out_str


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        prog="sacsim",
        description="Simulador de financiamento SAC",
        epilog="Valores de prestação aproximados. Não são considerados possíveis taxas mensais do banco.")
    
    parser.add_argument("valor_imovel", help="Valor de negociação do imóvel, em reais")
    parser.add_argument("valor_entrada", help="Valor de entrada na negociação")
    parser.add_argument("taxa_juro_anual", help="Taxa de juros anual, em porcentagem")
    parser.add_argument("n_parcelas", help="Número de parcelas mensais")
    parser.add_argument("-v", "--verbose", action="store_true", help="Detalhamento por parcela (opcional)")

    sacsim = SacSim(vars(parser.parse_args()))
    sacsim.run_simulation()

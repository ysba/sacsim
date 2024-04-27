import argparse

class SacSim:
    def __init__(self, input_val_dict):
        self.valor_imovel = float(input_val_dict["valor_imovel"])
        self.valor_entrada = float(input_val_dict["valor_entrada"])
        self.taxa_juro_anual = float(input_val_dict["taxa_juro_anual"])
        self.n_parcelas = int(input_val_dict["n_parcelas"])

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
        print("simulation loop init")
        valor_pago_total = self.valor_entrada
        valor_juros_total = 0

        print("simulation loop end")


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
    
    parser.add_argument("valor_imovel")
    parser.add_argument("valor_entrada")
    parser.add_argument("taxa_juro_anual")
    parser.add_argument("n_parcelas")

    sacsim = SacSim(vars(parser.parse_args()))
    sacsim.run_simulation()

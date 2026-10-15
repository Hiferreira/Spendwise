
# ============================================================
# SPENDWISE
# Gaste com inteligência. Economize melhor.
# Projeto desenvolvido com Python básico
# ============================================================


# -------------------- FUNÇÕES --------------------

def titulo(texto):
    print("\n" + "=" * 55)
    print(texto.center(55))
    print("=" * 55)


def ler_valor(mensagem, minimo=0):
    while True:
        try:
            entrada = input(mensagem).strip()
            entrada = entrada.replace(".", "").replace(",", ".")
            valor = float(entrada)

            if valor < minimo:
                print(f"Digite um valor igual ou superior a {minimo:.2f}.")
            else:
                return valor

        except ValueError:
            print("Valor inválido. Exemplo: 2500 ou 2500,50.")


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < minimo:
                print(f"Digite um número igual ou superior a {minimo}.")
            else:
                return valor

        except ValueError:
            print("Digite um número inteiro válido.")


def ler_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in ("sim", "s"):
            return True
        elif resposta in ("não", "nao", "n"):
            return False
        else:
            print("Resposta inválida. Digite sim ou não.")


def dinheiro(valor):
    return "R$ " + f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def cadastrar_gasto(lista, categoria, descricao, tipo):
    valor = ler_valor(f"{descricao} (R$): ")

    lista.append({
        "categoria": categoria,
        "descricao": descricao,
        "tipo": tipo,
        "valor": valor
    })

    return valor


# -------------------- INÍCIO DO SISTEMA --------------------

titulo("SPENDWISE")

print("Gaste com inteligência. Economize melhor.")
print("\nVamos organizar as finanças do mês.")

mes = input("\nQual mês você está organizando? ").strip()

if mes == "":
    mes = "Mês não informado"


# ============================================================
# 1. RENDA
# ============================================================

titulo("1. RENDA MENSAL")

salario = ler_valor(
    "Qual é sua renda líquida principal? R$ ",
    minimo=0.01
)

outras_rendas = 0

if ler_sim_nao("Você recebeu comissões ou outras rendas neste mês? (sim/não): "):
    quantidade_rendas = ler_inteiro(
        "Quantas outras fontes de renda deseja informar? ",
        minimo=1
    )

    for numero in range(1, quantidade_rendas + 1):
        print(f"\nRenda adicional {numero}")
        descricao = input("Descrição da renda: ").strip()

        if descricao == "":
            descricao = f"Renda adicional {numero}"

        valor = ler_valor("Valor recebido neste mês (R$): ")
        outras_rendas += valor

renda_total = salario + outras_rendas

print(f"\nRenda principal: {dinheiro(salario)}")
print(f"Rendas adicionais: {dinheiro(outras_rendas)}")
print(f"Renda total do mês: {dinheiro(renda_total)}")


# ============================================================
# 2. DESPESAS FIXAS
# ============================================================

titulo("2. DESPESAS FIXAS")

print("Informe os valores previstos para este mês.")
print("Se não possuir uma despesa, digite 0.")

despesas = []

total_fixas = 0

print("\n--- MORADIA ---")

total_fixas += cadastrar_gasto(
    despesas, "Moradia", "Aluguel ou financiamento", "Fixo"
)

print("\n--- ALIMENTAÇÃO PLANEJADA ---")

total_fixas += cadastrar_gasto(
    despesas, "Alimentação", "Orçamento de mercado", "Fixo planejado"
)

total_fixas += cadastrar_gasto(
    despesas, "Alimentação", "Orçamento de feira", "Fixo planejado"
)

print("\n--- TRANSPORTE ---")

total_fixas += cadastrar_gasto(
    despesas, "Transporte", "Transporte público mensal", "Fixo"
)

print("\n--- SAÚDE ---")

total_fixas += cadastrar_gasto(
    despesas, "Saúde", "Plano de saúde", "Fixo"
)

total_fixas += cadastrar_gasto(
    despesas, "Saúde", "Plano odontológico", "Fixo"
)

print("\n--- EDUCAÇÃO ---")

total_fixas += cadastrar_gasto(
    despesas, "Educação", "Faculdade", "Fixo"
)

total_fixas += cadastrar_gasto(
    despesas, "Educação", "Mensalidades de cursos", "Fixo"
)


# ============================================================
# 3. GASTOS VARIÁVEIS DO MÊS
# ============================================================

titulo("3. GASTOS VARIÁVEIS DO MÊS")

print(
    "Consulte seus registros e informe quanto gastou "
    "ou pretende gastar neste mês em cada categoria."
)

total_variaveis = 0
total_variaveis_essenciais = 0
total_opcionais = 0

print("\n--- MORADIA ---")

valor = cadastrar_gasto(
    despesas, "Moradia", "IPTU e impostos da propriedade", "Variável"
)
total_variaveis += valor

valor = cadastrar_gasto(
    despesas, "Moradia", "Manutenção e reparos", "Variável"
)
total_variaveis += valor

print("\n--- ALIMENTAÇÃO ---")

valor = cadastrar_gasto(
    despesas, "Alimentação", "Delivery", "Variável opcional"
)
total_variaveis += valor
total_opcionais += valor

valor = cadastrar_gasto(
    despesas, "Alimentação", "Restaurantes e lanches", "Variável opcional"
)
total_variaveis += valor
total_opcionais += valor

print("\n--- TRANSPORTE ---")

valor = cadastrar_gasto(
    despesas, "Transporte", "Uber e táxi", "Variável"
)
total_variaveis += valor

valor = cadastrar_gasto(
    despesas, "Transporte", "Combustível e outros deslocamentos", "Variável"
)
total_variaveis += valor

print("\n--- SAÚDE ---")

valor = cadastrar_gasto(
    despesas, "Saúde", "Medicamentos", "Variável essencial"
)
total_variaveis += valor
total_variaveis_essenciais += valor

valor = cadastrar_gasto(
    despesas, "Saúde", "Consultas e exames avulsos", "Variável essencial"
)
total_variaveis += valor
total_variaveis_essenciais += valor

print("\n--- EDUCAÇÃO ---")

valor = cadastrar_gasto(
    despesas, "Educação", "Livros e materiais", "Variável"
)
total_variaveis += valor

valor = cadastrar_gasto(
    despesas, "Educação", "Cursos avulsos", "Variável"
)
total_variaveis += valor

print("\n--- CUIDADOS PESSOAIS ---")

valor = cadastrar_gasto(
    despesas, "Cuidados pessoais", "Higiene e cosméticos", "Variável"
)
total_variaveis += valor
total_opcionais += valor

valor = cadastrar_gasto(
    despesas, "Cuidados pessoais", "Roupas e calçados", "Variável"
)
total_variaveis += valor
total_opcionais += valor

valor = cadastrar_gasto(
    despesas, "Cuidados pessoais", "Salão e outros cuidados", "Variável"
)
total_variaveis += valor
total_opcionais += valor


# ============================================================
# 4. LAZER
# ============================================================

titulo("4. LAZER")

lazer = cadastrar_gasto(
    despesas, "Lazer", "Lazer, passeios e viagens", "Variável opcional"
)

total_variaveis += lazer
total_opcionais += lazer

limite_lazer = renda_total * 0.10

print(f"\nReferência de 10% da renda: {dinheiro(limite_lazer)}")

if lazer > limite_lazer:
    print("Atenção: seu gasto com lazer ultrapassa a referência de 10%.")
    print(f"Excedente: {dinheiro(lazer - limite_lazer)}")
else:
    print("Seu gasto com lazer está dentro da referência de 10%.")


# ============================================================
# 5. COMPRAS PARCELADAS NO CARTÃO
# ============================================================

titulo("5. COMPRAS PARCELADAS")

print(
    "Informe compras parceladas que ainda comprometem "
    "sua renda. Não inclua novamente compras já somadas "
    "nos gastos variáveis acima."
)

compras = []

total_parcelas_mes = 0
total_compromisso_futuro = 0

if ler_sim_nao("Você possui compras parceladas no cartão? (sim/não): "):

    quantidade_compras = ler_inteiro(
        "Quantas compras parceladas deseja registrar? ",
        minimo=1
    )

    for numero in range(1, quantidade_compras + 1):

        print(f"\n--- COMPRA PARCELADA {numero} ---")

        descricao = input("Nome da compra: ").strip()

        if descricao == "":
            descricao = f"Compra parcelada {numero}"

        valor_compra = ler_valor(
            "Valor total da compra (R$): ",
            minimo=0.01
        )

        numero_parcelas = ler_inteiro(
            "Em quantas vezes foi parcelada? ",
            minimo=1
        )

        parcelas_pagas = ler_inteiro(
            "Quantas parcelas já foram pagas? ",
            minimo=0
        )

        while parcelas_pagas > numero_parcelas:
            print("As parcelas pagas não podem superar o total.")
            parcelas_pagas = ler_inteiro(
                "Quantas parcelas já foram pagas? ",
                minimo=0
            )

        valor_parcela = valor_compra / numero_parcelas
        parcelas_restantes = numero_parcelas - parcelas_pagas

        if parcelas_restantes > 0:
            total_parcelas_mes += valor_parcela
            total_compromisso_futuro += valor_parcela * parcelas_restantes

        compras.append({
            "descricao": descricao,
            "valor_total": valor_compra,
            "parcelas": numero_parcelas,
            "pagas": parcelas_pagas,
            "restantes": parcelas_restantes,
            "valor_parcela": valor_parcela
        })

        print(f"Valor de cada parcela: {dinheiro(valor_parcela)}")
        print(f"Parcelas restantes: {parcelas_restantes}")
        print(
            "Saldo futuro estimado desta compra: "
            f"{dinheiro(valor_parcela * parcelas_restantes)}"
        )


# ============================================================
# 6. DÍVIDAS ATIVAS
# ============================================================

titulo("6. DÍVIDAS ATIVAS")

dividas = []
total_pagamentos_dividas = 0

if ler_sim_nao("Você possui dívidas ativas além das compras parceladas registradas? (sim/não): "):

    quantidade_dividas = ler_inteiro(
        "Quantas dívidas deseja registrar? ",
        minimo=1
    )

    for numero in range(1, quantidade_dividas + 1):

        print(f"\n--- DÍVIDA {numero} ---")

        nome = input("Tipo de dívida: ").strip()

        if nome == "":
            nome = f"Dívida {numero}"

        saldo_devedor = ler_valor(
            "Saldo total devedor (R$): "
        )

        juros = ler_valor(
            "Taxa de juros mensal (%). Se não souber, digite 0: "
        )

        pagamento = ler_valor(
            "Pagamento obrigatório neste mês (R$): "
        )

        atrasada = ler_sim_nao(
            "A dívida está atrasada? (sim/não): "
        )

        dividas.append({
            "nome": nome,
            "saldo": saldo_devedor,
            "juros": juros,
            "pagamento": pagamento,
            "atrasada": atrasada
        })

        total_pagamentos_dividas += pagamento

    dividas.sort(
        key=lambda divida: (divida["atrasada"], divida["juros"]),
        reverse=True
    )

    print("\nPrioridade sugerida para avaliar a quitação:")

    for divida in dividas:
        if divida["atrasada"]:
            prioridade = "Dívida atrasada: verificar urgência e consequências"
        elif divida["juros"] >= 5:
            prioridade = "Juros mensais muito elevados"
        elif divida["juros"] >= 2:
            prioridade = "Juros mensais elevados"
        elif divida["juros"] > 0:
            prioridade = "Comparar com as demais dívidas"
        else:
            prioridade = "Taxa desconhecida ou sem juros informados"

        print(f"\n{divida['nome']}: {prioridade}")
        print(f"Saldo devedor: {dinheiro(divida['saldo'])}")
        print(f"Pagamento mensal: {dinheiro(divida['pagamento'])}")

    print(
        "\nA ordem é uma indicação inicial. Verifique as condições "
        "de quitação, os juros efetivos e as consequências dos atrasos."
    )

else:
    print("Nenhuma outra dívida ativa informada.")


# ============================================================
# 7. RESUMO DO COMPROMETIMENTO MENSAL
# ============================================================

titulo("7. COMPROMETIMENTO DA RENDA")

total_fixas_pagas = total_fixas

# As parcelas e os pagamentos de dívidas são compromissos mensais.
# Não somamos o valor integral das compras parceladas ao orçamento.
total_comprometido = (
    total_fixas_pagas
    + total_parcelas_mes
    + total_pagamentos_dividas
)

saldo_antes_variaveis = renda_total - total_comprometido

total_despesas_mes = (
    total_fixas_pagas
    + total_variaveis
    + total_parcelas_mes
    + total_pagamentos_dividas
)

saldo_final = renda_total - total_despesas_mes

print(f"\nMês analisado: {mes}")
print(f"Renda total: {dinheiro(renda_total)}")
print(f"Despesas fixas planejadas: {dinheiro(total_fixas_pagas)}")
print(f"Parcelas de compras: {dinheiro(total_parcelas_mes)}")
print(f"Pagamentos de outras dívidas: {dinheiro(total_pagamentos_dividas)}")
print(f"Total comprometido antes dos variáveis: {dinheiro(total_comprometido)}")

if renda_total > 0:
    percentual_comprometido = total_comprometido / renda_total * 100
else:
    percentual_comprometido = 0

print(f"Percentual comprometido: {percentual_comprometido:.2f}%")

print(f"\nGastos variáveis registrados: {dinheiro(total_variaveis)}")
print(f"Saldo mensal estimado: {dinheiro(saldo_final)}")

print(f"\nSaldo antes dos gastos variáveis: {dinheiro(saldo_antes_variaveis)}")

if saldo_final < 0:
    print("\nATENÇÃO: suas despesas superam sua renda.")
    print(f"Déficit estimado: {dinheiro(abs(saldo_final))}")
    print(
        "Antes de planejar novos aportes, precisamos revisar "
        "as despesas e os compromissos financeiros."
    )

elif saldo_final == 0:
    print("\nSeu orçamento está equilibrado, sem saldo livre.")

else:
    print("\nSeu orçamento apresenta saldo positivo.")
    print(
        "Esse saldo é uma estimativa com base nos valores informados. "
        "Reserve dinheiro para despesas ainda não registradas."
    )


# ============================================================
# 8. RESERVA DE EMERGÊNCIA
# ============================================================

titulo("8. RESERVA DE EMERGÊNCIA")

possui_reserva = ler_sim_nao(
    "Você já possui uma reserva de emergência? (sim/não): "
)

if possui_reserva:
    reserva_atual = ler_valor(
        "Quanto você tem guardado? R$ "
    )
else:
    reserva_atual = 0
    print("Vamos considerar que sua reserva atual é R$ 0,00.")

# Estimativa de despesas essenciais:
# despesas fixas + gastos variáveis de saúde.
# Os pagamentos obrigatórios de dívidas são considerados à parte.
despesas_essenciais = total_fixas_pagas + total_variaveis_essenciais

meta_tres_meses = despesas_essenciais * 3
meta_seis_meses = despesas_essenciais * 6

print(f"\nDespesas essenciais estimadas: {dinheiro(despesas_essenciais)}")
print(f"Meta inicial de 3 meses: {dinheiro(meta_tres_meses)}")
print(f"Meta de referência de 6 meses: {dinheiro(meta_seis_meses)}")
print(f"Reserva atual: {dinheiro(reserva_atual)}")

faltante = max(0, meta_seis_meses - reserva_atual)

print(f"Valor que falta para a meta de 6 meses: {dinheiro(faltante)}")

if meta_seis_meses > 0:
    progresso = min(100, reserva_atual / meta_seis_meses * 100)
    print(f"Progresso da meta: {progresso:.2f}%")

if faltante == 0:
    print("\nVocê já alcançou a meta de referência da reserva.")

elif saldo_final <= 0:
    print(
        "\nNão vamos sugerir uma contribuição agora, pois "
        "o orçamento está sem saldo positivo."
    )

elif dividas:
    print(
        "\nVocê possui dívidas ativas. Antes de definir uma contribuição, "
        "avalie se vale priorizar a quitação das dívidas com juros elevados, "
        "sem comprometer despesas essenciais e pagamentos obrigatórios."
    )

    if ler_sim_nao("Deseja simular um valor mensal para a reserva? (sim/não): "):
        contribuicao = ler_valor(
            "Quanto deseja guardar por mês? R$ ",
            minimo=0.01
        )

        if contribuicao > saldo_final:
            print(
                "Esse valor ultrapassa o saldo estimado. "
                "Informe um valor menor para fazer a simulação."
            )
        else:
            print(f"Contribuição simulada: {dinheiro(contribuicao)}")
            print(
                "Considere comparar essa proposta com a possibilidade "
                "de quitar dívidas caras."
            )

else:
    if ler_sim_nao("Deseja simular uma contribuição mensal? (sim/não): "):
        contribuicao = ler_valor(
            "Quanto deseja guardar por mês? R$ ",
            minimo=0.01
        )

        if contribuicao > saldo_final:
            print(
                "A contribuição supera o saldo estimado. "
                "Informe um valor menor."
            )
        else:
            meses = faltante / contribuicao

            print(f"\nContribuição mensal: {dinheiro(contribuicao)}")
            print(f"Tempo estimado para atingir a meta: {meses:.1f} meses")
            print(
                "A estimativa não considera rendimentos, saques "
                "ou mudanças futuras na renda e nas despesas."
            )


# ============================================================
# 9. RESUMO DAS COMPRAS PARCELADAS
# ============================================================

titulo("9. COMPROMISSOS FUTUROS DO CARTÃO")

print(f"Parcelas mensais registradas: {dinheiro(total_parcelas_mes)}")
print(
    "Saldo estimado das parcelas futuras registradas: "
    f"{dinheiro(total_compromisso_futuro)}"
)

if compras:
    print("\nDetalhamento:")

    for compra in compras:
        print(
            f"{compra['descricao']}: "
            f"{compra['restantes']} parcelas de "
            f"{dinheiro(compra['valor_parcela'])}"
        )

print(
    "\nImportante: esta versão mantém os dados apenas durante a execução. "
    "O salvamento por mês será uma próxima etapa do projeto."
)

titulo("FIM DO DIAGNÓSTICO")
print("Obrigado por utilizar o Spendwise!")
print("Gaste com inteligência. Economize melhor.")


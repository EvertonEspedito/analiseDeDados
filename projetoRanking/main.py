import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. DADOS
# =========================
dados = [
    ("Pedro Lucas Souza Santos Moraes", 425),
    ("Victor Gabriel Carvalho Souza", 0),
    ("Adrian Felipe de Amorim Oliveira", 545),
    ("Raquel Santos Conceição", 475),
    ("Lucas Pereira Mota", 470),
    ("Marina Joaquina de Lima Ferreira", 450),
    ("Deillon Jhon Alves", 470),
    ("Pamela Alice Barbosa Ribeiro da Silva", 0),
    ("Marcos Vinicius Freitas Trindade", 640),
    ("Pedro Gabriel Almeira Piaia", 470),
    ("Ray Gustavo Oliveira Siqueira", 435),
    ("Ismael Leite Rodrigues Nunes", 0),
    ("Luan Gabriel Nunez Diniz", 400),
    ("Breno dos Reis Dias", 350),
    ("João Gabriel de Araújo Alves", 415),
    ("Sophia de Andrade Alves", 55),
    ("Andrey Marlon Barbosa Ribeiro Da Silva", 0),
    ("Marcelo de Castro Marques Vanzo", 490),
    ("Deivid Cassiano Quezado de Lima", 335),
    ("Diogo Coelho Amorim", 475),
    ("Luigi Gustavo Moreira Souza", 220),
    ("Ingrid Maria dos Santos Vieira", 385),
]

df = pd.DataFrame(dados, columns=["Nome", "Total"])

# =========================
# 2. ANÁLISE EXPLORATÓRIA
# =========================
print("\n📌 Estatísticas gerais:")
print(df["Total"].describe())

total_participantes = len(df)
ativos = len(df[df["Total"] > 0])
inativos = len(df[df["Total"] == 0])

print(f"\n👥 Total de participantes: {total_participantes}")
print(f"✅ Participantes ativos: {ativos}")
print(f"❌ Participantes sem pontuação: {inativos}")

# =========================
# 3. CLASSIFICAÇÃO DE DESEMPENHO
# =========================
def classificar(pontos):
    if pontos >= 500:
        return "Excelente"
    elif pontos >= 400:
        return "Bom"
    elif pontos >= 200:
        return "Regular"
    elif pontos > 0:
        return "Baixo"
    else:
        return "Inativo"

df["Desempenho"] = df["Total"].apply(classificar)

print("\n📊 Distribuição por desempenho:")
print(df["Desempenho"].value_counts())

# =========================
# 4. RANKING
# =========================
ranking = df.sort_values(by="Total", ascending=False).reset_index(drop=True)
ranking.index += 1
ranking.insert(0, "Posição", ranking.index)

ranking.to_csv("ranking.csv", index=False)
print("\n📁 Ranking salvo em 'ranking.csv'")

# =========================
# 5. VISUALIZAÇÕES
# =========================

# Top 10
top10 = ranking.head(10)
plt.figure(figsize=(10,6))
plt.barh(top10["Nome"], top10["Total"])
plt.xlabel("Pontuação")
plt.ylabel("Nome")
plt.title("Top 10 - Pontuação")
plt.gca().invert_yaxis()
plt.show()

# Distribuição das pontuações
plt.figure(figsize=(8,5))
plt.hist(df["Total"], bins=10)
plt.xlabel("Pontuação")
plt.ylabel("Quantidade de participantes")
plt.title("Distribuição das Pontuações")
plt.show()

# Desempenho (contagem)
df["Desempenho"].value_counts().plot(kind="bar", figsize=(8,5))
plt.xlabel("Categoria de desempenho")
plt.ylabel("Quantidade")
plt.title("Distribuição de Desempenho")
plt.show()

# =========================
# 6. RESULTADO FINAL
# =========================
print("\n🏆 Ranking completo:")
print(ranking)

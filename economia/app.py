import requests

url = "http://127.0.0.1:8000/indicadores/api/"

r = requests.get(url)

if r.status_code == 200:
    dados = r.json()
    print("📌 Indicadores recebidos:")
    for i in dados:
        print(
            f"ID: {i['id']}, "
            f"Nome: {i['nome']}, "
            f"Categoria: {i['categoria']}, "
            f"Valor: {i['valor']}, "
            f"Quantidade: {i['quantidade']}, "
            f"Lucro (%): {i['percentual_lucro']}"
        )
else:
    print("Erro:", r.status_code)

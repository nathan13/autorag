import re
import os

class TextProcessor:

    @staticmethod
    def ler_testes_arquivo(caminho_arquivo):
        # Lê o arquivo e retorna o conteúdo
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        # Extrai todos os valores no novo padrão
        valores = re.findall(r'Teste\s*\d+:\s*([\d\.]+)m', conteudo)

        # Converte os valores para float
        valores = [float(valor) for valor in valores]

        return valores
    
    @staticmethod
    def calcular_estatisticas(valores):
        # Calcula a média
        media = sum(valores) / len(valores) if valores else 0
        
        # Encontra o maior e o menor valor
        maior_valor = max(valores) if valores else None
        menor_valor = min(valores) if valores else None
        
        return media, maior_valor, menor_valor

    @staticmethod
    def encontrar_testes_maior_menor(valores):
        # Encontra o índice dos testes com o maior e menor valor
        maior_teste = valores.index(max(valores)) + 1  # +1 para contar a partir do Teste 1
        menor_teste = valores.index(min(valores)) + 1
        
        return maior_teste, menor_teste

    @staticmethod
    def atualizar_arquivo(caminho_arquivo, total_testes, media, maior_valor, menor_valor, maior_teste, menor_teste):
        # Lê o conteúdo existente
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
            
            # Remove a seção de análise antiga se existir
            nova_conteudo = []
            incluir = True
            for linha in linhas:
                if '--- Análise Atualizada ---' in linha:
                    incluir = False
                if incluir:
                    nova_conteudo.append(linha)
                if not incluir and linha.strip() == '':
                    incluir = True
            
            # Adiciona a nova análise no topo
            nova_conteudo = [
                '--- Análise Atualizada ---\n',
                f"Total de testes: {total_testes}\n",
                f"Média dos valores: {media:.2f}\n",
                f"Maior valor: {maior_valor} (Teste {maior_teste})\n",
                f"Menor valor: {menor_valor} (Teste {menor_teste})\n",
                '\n'
            ] + nova_conteudo
        
            # Escreve o novo conteúdo no arquivo
            with open(caminho_arquivo, 'w') as arquivo:
                arquivo.writelines(nova_conteudo)
        else:
            # Se o arquivo não existir, cria um novo com a análise
            with open(caminho_arquivo, 'w') as arquivo:
                arquivo.write('--- Análise Atualizada ---\n')
                arquivo.write(f"Total de testes: {total_testes}\n")
                arquivo.write(f"Média dos valores: {media:.2f}\n")
                arquivo.write(f"Maior valor: {maior_valor} (Teste {maior_teste})\n")
                arquivo.write(f"Menor valor: {menor_valor} (Teste {menor_teste})\n")
                arquivo.write('\n')

    @staticmethod
    def salvar_texto_no_arquivo(caminho_arquivo, texto):
        # Verifica se o arquivo já existe
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()

            # Verifica quantos "Teste" já existem no arquivo
            contador = sum(1 for linha in linhas if linha.startswith("Teste"))
        else:
            contador = 0

        # Incrementa o contador para o novo teste
        contador += 1

        # Escreve o novo teste no arquivo
        with open(caminho_arquivo, 'a') as arquivo:
            arquivo.write(f"Teste {contador}:\n")
            arquivo.write(f"{texto}\n\n")


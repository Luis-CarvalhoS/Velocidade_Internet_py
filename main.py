import speedtest  # importa a biblioteca Speedtest para realizar o teste de velocidade
import time  # importa a biblioteca time para fazer pausas no código

def teste_velocidade(localizacao, provedor):
    print("Iniciando teste de velocidade...")  # imprime mensagem indicando que o teste está sendo iniciado
    teste = speedtest.Speedtest()  # cria um objeto Speedtest para realizar o teste
    print("Carregando lista de servidores...")  # imprime mensagem indicando que a lista de servidores está sendo carregada
    teste.get_servers()  # carrega a lista de servidores
    print("Escolhendo melhor rota...")  # imprime mensagem indicando que a melhor rota está sendo escolhida
    melhor_servidor = teste.get_best_server()  # escolhe o melhor servidor com base na latência
    print(f"Servidor encontrado: {melhor_servidor['host']} em {melhor_servidor['country']}, {melhor_servidor['name']}")  # imprime o servidor escolhido
    
    print("Performando teste de DOWNLOAD...")  # imprime mensagem indicando que o teste de download está sendo realizado
    download_resultado = teste.download()  # realiza o teste de download
    print("Teste de DOWNLOAD concluido!")  # imprime mensagem indicando que o teste de download foi concluído
    time.sleep(1)  # pausa o código por 1 segundo
    
    print("Performando teste de UPLOAD...")  # imprime mensagem indicando que o teste de upload está sendo realizado
    upload_resultado = teste.upload()  # realiza o teste de upload
    print("Teste de UPLOAD concluido!")  # imprime mensagem indicando que o teste de upload foi concluído
    time.sleep(1)  # pausa o código por 1 segundo
    
    ping_resultado = teste.results.ping  # obtém o ping do teste realizado
    
    # imprime o resultado do teste de velocidade com formatação
    print("\nResultado do teste de velocidade:")
    print(f"{'='*50}")
    print(f"{'Velocidade de Download:':<25} {download_resultado / 1024 / 1024:.2f} Mbit/s")
    print(f"{'Velocidade de Upload:':<25} {upload_resultado / 1024 / 1024:.2f} Mbit/s")
    print(f"{'Ping:':<25} {ping_resultado:.2f} ms")
    print(f"{'Provedor de Internet:':<25} {provedor}")
    print(f"{'='*50}")

# chama a função de teste de velocidade com a localização e provedor especificados
teste_velocidade('brazil', 'ex: claro, vivo fibra...')

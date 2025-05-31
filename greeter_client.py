import grpc
# Importa as classes geradas
import greeter_pb2
import greeter_pb2_grpc
def run():
# Estabelece um canal inseguro com o servidor (sem TLS neste exemplo)
# 'localhost:50051' é o endereço onde o servidor está escutando
    with grpc.insecure_channel('localhost:50051') as channel:
    # Cria um stub (cliente) usando o canal
        stub = greeter_pb2_grpc.GreeterStub(channel)
    # Cria a mensagem de requisição
        request_message = greeter_pb2.HelloRequest(name='Mundo')
    # Chama o método remoto SayHello usando o stub
        print("Chamando SayHello...")
        response = stub.SayHello(request_message)
    # Imprime a resposta recebida do servidor
        print(f"Resposta do servidor: {response.message}")

if __name__ == '__main__':
    run()

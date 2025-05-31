import grpc
from concurrent import futures
import time
# Importa as classes geradas
import greeter_pb2
import greeter_pb2_grpc
# Cria uma classe que herda do Servicer gerado e implementa o método
class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Recebida requisição de: {request.name}")
        return greeter_pb2.HelloReply(message=f'Olá, {request.name}!')
def serve():
    # Cria uma instância do servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Adiciona a implementação do serviço ao servidor
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    # Define a porta em que o servidor vai escutar
    server.add_insecure_port('[::]:50051')
    # Inicia o servidor
    print('Iniciando servidor na porta 50051...')
    server.start()
    # Mantém o servidor rodando
    try:
        while True:
            time.sleep(86400) # Um dia em segundos
    except KeyboardInterrupt:
        server.stop(0)
        
if __name__ == '__main__':
    serve()
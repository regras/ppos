#import das bibliotecas
import time, datetime, os

#captura do tempo local
x = float(time.mktime(datetime.datetime.now().timetuple()))

#leitura do arquivo node
with open("node.py", "r") as node:
    file = node.readlines()
file[2167] = "    startTime = " + str(int(x)) + '\n'

#escrita do tempo
with open("node.py", 'w') as node:
    node.writelines(file)

#chamadas de sistema

#checagem de containers existentes
os.system("rm script-output.txt")
os.system("docker service rm cpos_cpos > script-output.txt")
check = os.path.getsize('script-output.txt')
if check > 0:
    time.sleep(20)

#criacao de novos containers
os.system("docker network rm netcpos")
os.system("docker image rm cpos")
os.system("docker network create --driver overlay --subnet 10.1.0.0/22 --gateway 10.1.0.1 netcpos")
os.system("touch tx.txt")
os.system("rm peers.pkl && python2 topology.py")
os.system("docker build -t cpos .")
os.system("docker stack deploy --compose-file docker-compose.yml cpos")

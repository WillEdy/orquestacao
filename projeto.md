Professor não consegui passar da criação do container da aplicação, realizei várias tentativas de build de imagem todas com falha... 
Sempre retornando o erro CrashLoopBackOff 
![alt text](orquestracao/images/CrashLoopBackOff.png)

E também não sei o porque não consegui visualizar os logs
![alt text](orquestracao/images/noLogs.png)

Porém realizei o push das imagens para o dockerhub 
![alt text](orquestracao/images/login_docker_hub.png)

![alt text](orquestracao/images/repositorios_docker.png)

Ao tentar adicionar volumes persitente ou utilizar o statefullset como nos exemplos sempre recebi esse erro... 

"Error from server (BadRequest): error when creating "deploy-infra.yaml": Deployment in version "v1" cannot be handled as a Deployment: strict decoding error: unknown field "spec.status", unknown field "spec.template.spec.contain"

Pesquisando acredito que seja a versão do kubernetes que eu estava usando, tentei subir o minikube em outras versões porém todas sem sucesso... 

Tentei ajustas os problemas sem sucesso, esse mês de abril foi muito puxado em todos os aspectos, sei que o senhor sempre esteve disponível para ajudar mas eu não estava com tempo... 
Me desculpe ...
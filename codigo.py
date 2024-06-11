#Funções

#dados pessoa
def dados_pessoa():   
        dadosPessoa = []     
        nome = input('Digite seu nome: ')      
        while len(nome) == 0: #validação de dados 
            print("Nome inválido. Tente novamente.")
            nome = input('Digite seu nome: ')
            dadosPessoa.append(nome)
        
        cpf = input('Digite seu CPF: ')
        while len(cpf) != 11: #validação de dados 
            print("CPF inválido. Digite um CPF válido(somente números).")
            cpf = input('Digite seu CPF: ')
            dadosPessoa.append(cpf)

        telefone = input('Digite seu telefone (Incluir DDD): ') 
        while len(telefone) == 0 or len(telefone) != 11: #validação de dados 
            print("Telefone inválido. Tente novamente.")
            telefone = input('Digite seu telefone (Incluir DDD): ')
            dadosPessoa.append(telefone)

        email = input('Digite seu e-mail de contato: ')
        while len(email) == 0: #validação de dados
             print('O e-mail de contato é inválido. Tente novamente')
             email = input('e-mail de contato: ')
             dadosPessoa.append(email)

        print('\n*Dados do Cliente*')
        print(f'Nome: {nome}')
        print(f'CPF: {cpf}')
        print(f'Telefone: {telefone}')
        print(f'E-mail de contato: {email}')

#dados jurídico
def dados_empresa():   
        dadosEmpresa = []
        razaoSocial = input('Qual a Razão Social: ')
        while len(razaoSocial) == 0: #validação de dados
            print("A razão social é inválida. Tente novamente.")
            razaoSocial = input('Qual a Razão Social: ') 
            dadosEmpresa.append(razaoSocial)

        cnpj = input('Qual o CNPJ (somente número): ')
        while len(cnpj) !=14: #validação de dados 
            print("O cnpj é inválido. Tente novamente.")
            cnpj = input('Qual o CNPJ: ')  
            dadosEmpresa.append(cnpj)     
        
        insEstadual = input('Qual a Inscrição Estadual: ')
        while insEstadual == 0: #validação de dados 
            print("Inscrição Estadual está inválida. Tente novamente.")
            insEstadual = input('Qual a inscrição Estadual: ') 
            dadosEmpresa.append(insEstadual)
        
        contato = input('Telefone de contato (Incluir DDD): ')
        while len(contato) == 0:  #validação de dados
            print("O contato está inválido. Tente novamente.")
            contato = input('Telefone de contato (Incluir DDD): ')
            dadosEmpresa.append(contato)

        email = input('Digite seu e-mail de contato: ')
        while len(email) == 0: #validação de dados
             print('O e-mail de contato é inválido. Tente novamente')
             email = input('e-mail de contato: ')
             dadosEmpresa.append(email)
             

        print('\n*Dados Jurídico*')
        print(f'Razão Social: {razaoSocial}')
        print(f'CPNJ: {cnpj}')
        print(f'Inscrição Estadual: {insEstadual}')
        print(f'Contato: {contato}')  
        print(f'E-mail de contato: {email}')

        print('Obrigado por ter entrado em contato, retornaremos um e-mail para te informar sobre a disponibilidade de contribuidor')    

#Denúncia
def dados_denuncia():
        dadosDenuncia = []
        localDenuncia = input('Local de denúncia de poluição: ')
        while len(localDenuncia) == 0: #validação de dados
             print('O local está inválido. Tente novamente')
             localDenuncia = input('Local de denúncia de poluição inválido. Tente novamente')
             dadosDenuncia.append(localDenuncia)
    
        descrDenuncia = input('Descreva o tipo de denúncia verificado: ')
        while len(descrDenuncia) == 0: #validação de dados
             print('Descrição inválida. Tente novamente')
             descrDenuncia = input('Descreva o tipo de denúncia verificado: ')
             dadosDenuncia.append(descrDenuncia)

        print(f'\n*Dados da denúncia*')
        print(f'Local de denúncia: {localDenuncia}')
        print(f'Descrição da denúncia: {descrDenuncia}')


#Acompanhamento de Denúncia
def dados_acompanhamento():
        dadosAcompanhamento = []
        numDenuncia = int(input('Informe o número do chamado da sua denúncia: '))
        while numDenuncia == 0: #validação de dados
             print('Número de denúncia inválido. Tente novamente')
             numDenuncia = input('informe o número do chamado da sua denúncia: ')
             dadosAcompanhamento.append(numDenuncia)

        colabDenuncia = input('Informe o nome do colaborador que entrou em contato: ')
        while len(colabDenuncia) ==0: #validação de dados
             print('Colaborador inválido. Tente novamente')
             colabDenuncia = input('Informe o nome do colaborador que entrou em contato: ')
             dadosAcompanhamento.append(colabDenuncia)

        print('\n*Dados acompanhamento de denúncia*')
        print(f'Número da denúncia: {numDenuncia}')
        print(f'Colaborador: {colabDenuncia}')
     

#Poluição
def dados_poluicao():  
        dadosPoluicao = []          
        localPoluicao = input('Local que está com relatos de poluição: ')
        while len(localPoluicao) == 0:  #validação de dados
            print("O local está inválido. Tente novamente.")
            localPoluicao = input('Local que está com relatos de poluição: ')
            dadosPoluicao.append(localPoluicao)

        descrPoluicao = input('Qual o tipo de poluição encontrada: ')
        while len(descrPoluicao) == 0:  #validação de dados
            print("Descição inválida. Tente novamente.")
            descrPoluicao = input('Qual o tipo de poluição encontrada: ')
            dadosPoluicao.append(descrPoluicao)
        
        print('\n*Poluição apresentada*')
        print(f'Local com poluição: {localPoluicao}')
        print(f'Descrição da Poluição: {descrPoluicao}')  

        print('Obrigado por realizar a denúncia, iremos tomar as devidas providência')

#Redes de contato
def dados_contato():
     print('E-mail Geral: usuario@oceanhelper.com')
     print('Telefone: (11) 5555-5555')
     print('Instagram: @orgOceanHelper')
     print('Endereço: Av. Lins de Vasconcelos, 1222')

#Sensor via satélite
def dados_sensor():
        dadosSensor = []
        print('Os sensores de poluição serão ativados na localização informada')
        sensor = input('Digite a porcentagem relatada no sensor: ')
        if len(sensor) == 0:
             print('A localização se encontra em conduições normais, chamado encerrado')
        elif len(sensor) > 1 and len(sensor) <=30:
             print('Poluição detectada, para esse nível, será realizado o envio de drones para que seja feita a limpeza')
        else:
             print('Nível alto de poluição detectado, moveremos colaborados junto com nossos drones para que seja realizada a limpeza o mais rápido possível')
             dadosSensor.append(sensor)

#Atendente
def dados_atendente():
        dadosAtendente = []
        print('Opções disponíveis: ')
        print('1 - Tirar Dúvidas')
        print('2 - Relatar atraso para limpeza')
        print('3 - Outros')
        atendimento = input('Ação desejada: ')

        if atendimento == 1:
             print('Responda a questão a seguir:')
             duvida = input('Digite sua dúvida: ')
        
        elif atendimento == 2:
             print('Responda a questão a seguir:')
             atraso = input('Digite o número do chamado para que possamos localizar o atraso: ')
        
        else:
             print('Responda a questão a seguir: ')
             outro = input('Digite qual ação deseja realizar: ')
        dadosAtendente.append(atendimento)

        print(f'Dúvida:{duvida} ')
        print(f'Número chamado: {atraso}')
        print(f'Outro: {outro}')

#Voluntário
def dados_voluntario():
          dadosVoluntario = []
          print('Digite os dados para que possamos identificar a possibilidade de se candidatar para ser voluntário')
          localVoluntario = input('Qual o local de escolha para voluntariar: ')
          while len(localVoluntario) == 0: #validação de dados
               print('Local inválido. Tente novamente')
               localVoluntario = input('Qual o local de escolha para voluntariar: ')
               dadosVoluntario.append(localVoluntario)

          dispVoluntario = input('Digite a data de disponibilidade para voluntariar: ')
          while len(dispVoluntario) == 0: #validação de dados
               print('Disponibilidade inválida. Tente novamente')
               dispVoluntario = input('Digite a data de disponibilidade para voluntariar: ')
               dadosVoluntario.append(dispVoluntario)

          endVoluntario = input('Digite seu logradouro: ')
          while len(endVoluntario) == 0: #validação de dados
               print('Logradouro inválido. Tente novamente')
               endVoluntario = input('Digite seu logradouro: ') 
               dadosVoluntario.append(endVoluntario)

          numVoluntario = input('Digite o número: ')
          while numVoluntario == 0: #validação de dados
               print('Número inválido. Tente novamente')
               numVoluntario = input('Digite o número: ')
               dadosVoluntario.append(numVoluntario)

          cepVoluntario = input('Digite o CEP: ')
          while cepVoluntario == 0 and len(cepVoluntario) != 8: #validação de dados
               print('CEP inválido. Tente novamente')
               cepVoluntario = input('Digite o CEP: ')
               dadosVoluntario.append(cepVoluntario)

          kmVoluntario = input('Digite a quilometragem máxima de distância aceita para quando algum local estive com necessidade de voluntários: ')
          while kmVoluntario == 0: #validação de dados
               print('Quilometragem inválida. Tente novamente')
               kmVoluntario = input('Digite a quilometragem máxima de distância aceita para quando algum local estive com necessidade de voluntários: ')
               dadosVoluntario.append(kmVoluntario)

          print(f'Local desejado: {localVoluntario}')
          print(f'Disponibilidade do voluntário: {dispVoluntario}')
          print(f'Endereço do voluntário: {endVoluntario}')
          print(f'Número do endereço: {numVoluntario}')
          print(f'CEP: {cepVoluntario}')
          print(f'Quilometragem máxima de distância de voluntariado: {kmVoluntario}')

          print('Obrigado por ter entrado em contato, assim que houver uma campanha, encaminharemos todas informações por e-mail')

def ret_atendente():       
          print('Por gentileza, responda as perguntas: ')
          dados_atendente() 

def ret_contribuidor():
           #Pessoa Física ou Jurídica
            print('Informe os dados para verificarmos a possibilidade de ser um contribuidor:')
            print('1 - Pessoa física')
            print('2 - Pessoa jurídica')
            escPessoa = int(input('Digite sua escolha: '))
            if escPessoa == 1:
                 dados_pessoa()
                 print('Obrigado por ter entrado em contato, retornaremos um e-mail para te informar sobre a disponibilidade de contribuidor')
            else:
                 dados_empresa()
                 print('Obrigado por ter entrado em contato, retornaremos um e-mail para te informar sobre a disponibilidade de contribuidor')

def ret_poluicao():
           #Poluição - Retorno
            print('Informe os dados para iniciarmos a busca: ')
            dados_poluicao()
            dados_sensor()

def ret_denuncia():
           #Denuncia - Retorno
           print('Informe os dados para iniciarmos a busca: ')
           dados_denuncia()

def ret_acompanhamento():
           #Acompanhamento - Retorno
           print('Informe os dados para iniciarmos a busca: ')
           dados_acompanhamento()

def ret_voluntario():
             #Voluntario - Retorno
             print('Informe os dados para iniciarmos o processo: ')
             dados_pessoa()
             dados_voluntario()

def ret_redes():
           #Redes - Retorno
           print('Segue Redes de Contato: ')
           dados_contato()

#Principal
           #Chamado
def opcao_chamado():
     while True:
          #Escolha - Atendimento
          print('Opções disponíveis: ')
          print('1 - Falar com atendente')
          print('2 - Virar um contribuidor')
          print('3 - Relatar poluição')
          print('4 - Realizar denúncia')
          print('5 - Acompanhar relato de denúncia')
          print('6 - Virar voluntário')
          print('7 - Obter redes de contato')
          print('8 - Encerrar contato')

          escolha_chamado = int(input('Digite a opção desejada: '))

          resposta = processamento_chamado(escolha_chamado)
          print(resposta)

          #Para encerrar contato
          if escolha_chamado == '8':
               break

def processamento_chamado(escolha_chamado):
          if escolha_chamado == 1:
            print(f'Serviço solicitado: {escolha_chamado}')       
            ret_atendente() 

          elif escolha_chamado == 2:
            print(f'Serviço solicitado: {escolha_chamado}') 
            ret_contribuidor()

          elif escolha_chamado == 3:
            print(f'Serviço solicitado: {escolha_chamado}')       
            ret_poluicao()

          elif escolha_chamado == 4:
             print(f'Serviço solicitado: {escolha_chamado}')
             ret_denuncia()
        
          elif escolha_chamado == 5:
             print(f'Serviço solicitado: {escolha_chamado}')
             ret_acompanhamento()

          elif escolha_chamado == 6:
             print(f'Serviço solicitado: {escolha_chamado}')
             ret_voluntario()

          else:
             print(f'Serviço solicitado: {escolha_chamado}')
             ret_redes()

#Finalizar
print('Ocean Helper')
opcao_chamado()

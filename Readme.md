

 Processo seletivo programador - be3 health tech



## Descrição do Projeto 📄

<p>Um usuário deve conseguir cadastrar um novo paciente e editar um paciente existente mas não deve ser
possível excluir um cadastro.</p>

Versão do python utilizada no projeto: ![Python 3](https://img.shields.io/badge/python-3.8-blue.svg)



## Instalação 🛠️

Faça o clone do projeto.

```python
git clone https://github.com/Erickson-lopes-dev/be3-health-tech_Teste
cd be3-health-tech_Teste
```



Crie uma maquina virtual  para rodar o projeto.

```python
python3 -m venv venv
```

Uma vez criado seu ambiente virtual, você deve ativá-lo.

No Unix ou no MacOS, executa:

```
source venv/bin/activate
```

No Windows, execute:

```python
venv\Scripts\activate.bat
```



Com o ambiente virtual ativado, Instale as dependências (certifique-se de que esteja na mesma pasta que o arquivo).

```python
pip install -r requirements.txt
```



Antes de iniciar o projeto é necessário fazer as migrações das tabelas.

```
py manage.py migrate
```



E também criar um usuário !

```python
py manage.py createsuperuser

>>> Usuário (leave blank to use 'ofcer'):
>>> (Digite um nome de usuário apra login)

>>> Endereço de email:
>>> (Digite um enredeço de email)

>>> Password:
>>> (Digite uma senha)

>>> Password (again):
>>> (Digite novamente a senha)
```

Agora  que instalamos tudo, podemos iniciar !

## Exemplo de Funcionamento

Execute o arquivo do programa.

```python
py manage.py runserver

Após, basta clicar no link para ser redirecionado para o navegador
>>> http://127.0.0.1:8000/
```



Digite o nome do usuário e senha que foi criado para logar no sistema e clique em login.

<img src="C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601005122235.png" alt="image-20210601005122235" style="zoom: 80%;" />

Ao logar podemos nos deparamos com a dashboard do sistema, onde é possível observar a quantidade total de paciente e estatisticas que demostram a porcentagem que convênio tem referente ao todo.

<img src="C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601005826740.png" alt="image-20210601005826740" style="zoom:67%;" />

Clique em qualquer um dos lugares indicado,  você será redirecionado para onde se localiza uma lista que armazenará alguns dados dos pacientes para realizar pesquisas.

![image-20210601010608318](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601010608318.png)



Aqui sera exibido a lista com todos os dados disponiveis, onde é possível pelas barras de pesquisa encontrar um paciente digitando qualquer dados da coluna referente ao paciente.

![image-20210601010715546](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601010715546.png)



Clique em qualquer um dos lugares indicado,  você será redirecionado para página de adicionar novo registro de paciente

![image-20210601011408856](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601011408856.png)

(Redimensionei a tela para melhor visualização )

![image-20210601012039835](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601012039835.png)

![image-20210601012858702](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601012858702.png)

Na lista é possível obter todos os dados do paciente clicando no nome

![image-20210601012902143](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601012902143.png)

![image-20210601013106090](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601013106090.png)



E se caso você deseje editar os dados, temos duas opções para isso !

![image-20210601013201114](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601013201114.png)



Basta clicar e você sera redirecionado para o formulario, basta alterar os dados e salvar !

![image-20210601013326314](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601013326314.png)

e se olhar a dashboard, toda ação ja começou a acontecer, possível ver quais convênios os clientes mais usam!

![image-20210601013348249](C:\Users\ofcer\AppData\Roaming\Typora\typora-user-images\image-20210601013348249.png)




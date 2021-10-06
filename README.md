# student-management

Projeto com finalidade de implementar API que seja capaz de armazenar dados e editar dados de um estudantes no sistema.

# Table of contents
1. [Tecnologias](#technologies)
2. [Estrutura do Projeto](#project_structure)
3. [Estrutura do Banco](#database_structure)
4. [Setup Local](#localsetup)
5. [Execução](#project_run)
6. [Endpoints](#endpoints)
    - [Lista de estudantes](#students_list)
    - [Criar estudante](#student_create)
    - [Editar ou deletar estudante](#student_update_or_destroy)
7. [Execução dos Testes](#tests)

## Tecnologias <a name="technologies"></a>
    - Docker
    - Django
    - Django REST Framework
    - SQLite3

## Estrutura do Projeto <a name="project_structure"></a>

1. Projeto Django
2. Módulo de gerenciamento e configuração do projeto
3. Módulo referente aos estudantes
4. Arquivos de configuração do docker

## Estrutura do Banco <a name="database_structure"></a>
![Estrutura do banco](https://github.com/marcelacrosariol/student-management/blob/main/docs/estrutura_banco.png)


## Setup Local<a name="localsetup"></a>

Se ainda não possuir Docker instalado em sua máquina, [ siga as instruções da página da ferramenta para instalar a Engine e o Compose ](https://docs.docker.com/get-docker/).

1. Clone/baixe o projeto.

2. Crie um arquivo `.env` dentro do diretório raiz (student-management) com o seguinte conteúdo - este será necessário para definir as variáveis de ambiente acessadas pelo container.

```
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
DEBUG=1
```

3. Construa a imagem a ser utilizada pelo container com o seguinte comando:

```shell
$ docker-compose build
```

4. Execute as migrações para criar e preparar o banco de dados.

```shell
$ docker exec -it student-management-main_app_1 ./manage.py migrate
```

## Execução <a name="project_run"></a>

Para executar o container e acessar a API em sua máquina local, utilize o seguinte comando:

```shell
docker-compose up
```

## Endpoints <a name="endpoints"></a>

### `/students/` <a name="students_list"></a>
<_Lista estudantes_>

**Método** : `GET`

**URL Params (opcional)**: `search=[<name> ou <family_name> ou <student_id>]`

### Success Response

**Code** : `200 OK`

**Exemplo de saída**
```json
[
    {
        "name": "Marcela",
        "family_name": "Crosariol",
        "gender": "Feminino",
        "birthday": "1994-09-28",
        "student_id": "2020010001SP",
        "status": "Inativo"
    },
]
```
-------------------------------------------------------------------------------

### `/students/create/` <a name="student_create"></a>
<_Cria novo estudante_>

**Método** : `POST`

**Restrições*

```json
{
   "family_name":[
      "This field is required."
   ]
}
```

**Exemplo de Dado de Entrada**

```json
{
   "name":"Maria",
   "family_name":"da Silva",
   "birthday":"1998-02-16",
   "student_id":"2021010002SP"
}
```

### Exemplo de Requisição Bem Sucedida

**Code** : `201 CREATED`

**Content example**

```json
{
   "name":"Maria",
   "family_name":"da Silva",
   "birthday":"1998-02-16",
   "gender":0,
   "student_id":"2021010002SP",
   "status":0
}
```

### Exemplo de Requisição Falha (data em formato não-compatível)

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
   "birthday":[
      "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
   ]
}
```
-------------------------------------------------------------------------------
### `/students/<id>/` <a name="student_update_or_destroy"></a>
<_Edita ou deleta estudante_>

**Método** : `PUT`

**Exemplo de Dado de Entrada**

```json
{
   "name":"Marcela",
   "family_name":"Crosariol",
   "birthday":"1994-09-28",
   "student_id":"2021010001RJ"
}
```

### Exemplo de Requisição Bem Sucedida

**Code** : `200 OK`

**Content example**

```json
{
    "name": "Marcela",
    "family_name": "Crosariol",
    "birthday": "1994-09-28",
    "gender": 0,
    "student_id": "2021010001RJ",
    "status": 1
}
```

**Método** : `DELETE`

### Exemplo de Requisição Bem Sucedida

**Code** : `204 No Content`

-------------------------------------------------------------------------------

## Execução dos Testes <a name="tests"></a>
```
docker exec -it <container_name> ./manage.py test --verbosity=2]
```

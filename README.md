# CRUD Flask

Primeira API criada por mim utilizando Flask. Utilizando os conceitos adquiridos até agora na Kenzie Academy Brasil com um pouco de curiosidade consegui fazer uma API bem simples utilizando Flask. A API consiste num CRUD que persiste os dados em um arquivo CSV.

<br>

# Pré requisitos

## Python VENV

```
$ python3 -m venv venv
```

## Ativar VENV

```
$ . venv/bin/activate
```

## Flask

```
$ pip install Flask
```

<br>

# Rotas

Abaixo segue descrição das rotas e das requisições. Nenhuma das rotas necessita de autenticação.

## Listando personagens

`GET / - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "data": [
    {
      "agility": 8,
      "id": 1,
      "intelligence": 8,
      "name": "Hulk",
      "power": 7,
      "strength": 10
    },
    {
      "agility": 4,
      "id": 2,
      "intelligence": 4,
      "name": "Superman",
      "power": 5,
      "strength": 5
    }
  ],
  "message": "Characters found"
}
```

## Listando personagens específicos

`GET /character - FORMATO DA REQUISIÇÃO`

```json
{
  "character_id": 2
}
```

`GET /character - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "data": {
    "agility": 4,
    "id": 2,
    "intelligence": 4,
    "name": "Superman",
    "power": 10,
    "strength": 10
  },
  "message": "Character found"
}
```

## Criando personagens

`POST /create - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "Superman",
  "intelligence": 4,
  "power": 10,
  "strength": 10,
  "agility": 4
}
```

`POST /create - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "data": {
    "agility": 4,
    "id": 2,
    "intelligence": 4,
    "name": "Superman",
    "power": 10,
    "strength": 10
  },
  "message": "Character created"
}
```

## Atualizando personagens

`PATCH /update - FORMATO DA REQUISIÇÃO`

```json
{
  "character_id": 2,
  "power": 5,
  "strength": 5
}
```

`PATCH /update - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "data": {
    "agility": 4,
    "id": 2,
    "intelligence": 4,
    "name": "Superman",
    "power": 5,
    "strength": 5
  },
  "message": "Character updated"
}
```

## Deletando personagens

`DELETE /delete - FORMATO DA REQUISIÇÃO`

```json
{
  "character_id": 2
}
```

`DELETE /delete - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "data": true,
  "message": "Character deleted"
}
```

# Feito com

![Flask](https://img.shields.io/badge/-Flask-05122A?style=flat&logo=flask)&nbsp;

# Autor

Feito com ♥ por **Abdiel Martins** - [abdielmartins](https://github.com/abdielmartins)

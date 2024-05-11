# Criar uma aplicação motor de crédito

## Descrição
Dado um cliente que deseja fazer um empréstimo, precisamos criar uma aplicação que seja capaz de avaliar seu score de crédito seguindo as seguintes regras:

- O usuário fornecerá os seguintes dados: nome, idade, renda mensal e cidade.
- O score de crédito será calculado da seguinte forma.
```
score = componente de idade + componente de renda + componente de temperatura
```

- O componente de idade é calculado da seguinte forma:
```
componente de idade = idade * 0.5
```

- O componente de renda é calculado da seguinte forma:
```
componente de renda = (renda mensal/100) * 2
```

- O componente de temperatura é calculado da seguinte forma:
```
componente de temperatura = temperatura * 5
```

Exemplo de calculo:

```
idade = 30
renda mensal = 1800
temperatura = 30
componente de idade = 30 * 0.5 = 15
componente de renda = 1800/100 * 2 = 36
componente de temperatura = 30 * 5 = 150
score = 15 + 36 + 150 = 201
```

- O crédito será aprovado se o score for maior ou igual a 200 e a idade for maior ou igual a 18 anos.

- A temperatura será obtida através de uma API externa, que pode ser acessada através do seguinte endpoint open weather:
```
http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}
```
open weather response 
```json
{
  "coord": {
    "lon": -47.8908,
    "lat": -22.0175
  },
  "weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "broken clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 294.3,
    "feels_like": 294.01,
    "temp_min": 294.3,
    "temp_max": 294.3,
    "pressure": 1024,
    "humidity": 59,
    "sea_level": 1024,
    "grnd_level": 930
  },
  "visibility": 10000,
  "wind": {
    "speed": 5.81,
    "deg": 152,
    "gust": 6.78
  },
  "clouds": {
    "all": 54
  },
  "dt": 1689792500,
  "sys": {
    "country": "BR",
    "sunrise": 1689760155,
    "sunset": 1689799562
  },
  "timezone": -10800,
  "id": 3449319,
  "name": "São Carlos",
  "cod": 200
}
```

Para acessar a API é necessário criar uma conta e gerar uma chave de acesso.

# Resultado esperado

- Criar uma aplicação que seja capaz de receber os dados do usuário e retornar o score de crédito e se o crédito foi aprovado ou não.

# Requisitos
- A aplicação deve rodar de maneira local em Linux ou Windows.
- O candidato pode utilizar a interface com que melhor trabalhe (REST api, GraphQL, commandline e etc).
- A criação de validaçoes de dados é opcional, porém recomendada.
- A criação de testes unitários é obrigatória, é uma parte essencial do trabalho.
- A linguagem de programação é de escolha livre do candidato, porém recomendamos Java, Kotlin, Javascript, Python, Go, Dart ou Clojure.
- O candidato pode utilizar bibliotecas de terceiros, porém recomendamos que o código seja o mais simples possível.
- Não é necessário salvar os dados em um banco de dados, pode ser em memória.
- O código deve ser disponibilizado neste mesmo repositório.
- O Score é um número inteiro.
- O candidato deve criar um arquivo README explicando como rodar a aplicação, os testes unitários e utilizar a interface.

# Diferenciais
- O código da aplicação e dos teste unitários ser simples (bem organizado e fácil de entender) e funcional (no sentido de funcionar).

# Recomendações
O objetivo deste teste é ser conciso e que o candidato possa demonstrar habilidades que serão o dia a dia de trabalho mais básico na empresa. Também, o teste servirá de insumos para uma conversa técnica, onde o candidato poderá demonstrar habilidades mais avançadas e outros conhecimentos baseados na perceção e na evolução do sistema hipotético. Ou seja, a completude do sistema hipotético não é o objetivo, mas anote suas ideias para termos uma entrevista mais rica.

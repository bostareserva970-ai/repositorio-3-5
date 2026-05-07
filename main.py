class Pessoa:
    def __init__(self, nome, email, sexo, numero, cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.numero = numero
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Sexo: {self.sexo}")
        print(f"Número: {self.numero}")
        print(f"CPF: {self.cpf}")
        print("-" * 30)


pessoa1 = Pessoa(
    nome="João Silva",
    email="joao@email.com",
    sexo="Masculino",
    numero="61999999999",
    cpf="123.456.789-00"
)

pessoa2 = Pessoa(
    nome="Maria Oliveira",
    email="maria@email.com",
    sexo="Feminino",
    numero="61888888888",
    cpf="987.654.321-00"
)

pessoa1.exibir_dados()
pessoa2.exibir_dados()
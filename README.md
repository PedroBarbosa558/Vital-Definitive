# Vital-Definitive

Vital é uma aplicação web desenvolvida em Django para gerenciamento de exames médicos. A plataforma permite que pacientes solicitem exames, médicos acessem resultados e administradores gerenciem todo o processo.

## 🚀 Funcionalidades

### Para Pacientes
- Cadastro e login de usuários
- Solicitação de exames médicos
- Visualização dos exames solicitados
- Acesso aos resultados mediante senha

### Para Médicos
- Acesso aos resultados dos exames dos pacientes
- Gerenciamento de acessos médicos

### Para Administradores
- Gerenciamento completo de exames
- Controle de tipos de exames disponíveis
- Gerenciamento de preços e disponibilidade

## 💻 Tecnologias Utilizadas

- Python 3.12
- Django 5.0
- SQLite3
- HTML5
- CSS3
- JavaScript

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/PedroBarbosa558/Vital-Definitive.git
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

## 📋 Estrutura do Projeto

```
Vital-Definitive/
├── exames/                 # Aplicação de exames
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Lógica de negócio
│   ├── urls.py            # Rotas da aplicação
│   └── templates/         # Templates HTML
├── usuarios/              # Aplicação de usuários
├── templates/             # Templates globais
├── static/               # Arquivos estáticos
└── vital/                # Configurações do projeto
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Pedro Barbosa
- GitHub: [@PedroBarbosa558](https://github.com/PedroBarbosa558)

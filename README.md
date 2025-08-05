# Projeto Hamburgueria - Django

Este é um projeto de sistema web para uma hamburgueria, desenvolvido com Django Framework. O sistema permite gerenciar produtos, pedidos e oferece uma interface moderna para clientes realizarem pedidos online.

## Tecnologias Utilizadas

- **Python 3.12+**
- **Django 5.0.6**
- **Django Channels** (WebSockets para funcionalidades em tempo real)
- **Redis** (para gerenciamento de canais)
- **SQLite** (banco de dados)
- **HTML5, CSS3, JavaScript**
- **Webpack** (bundler para assets)

## Funcionalidades

### Sistema de Produtos
- Cadastro e gerenciamento de produtos
- Upload de imagens dos produtos
- Categorização de produtos
- Controle de preços e descontos
- Tempo de preparo estimado

### Sistema de Pedidos
- Interface de pedidos em tempo real
- Cálculo automático de frete
- WebSockets para atualizações instantâneas
- Status de pedidos
- Histórico de pedidos

### Funcionalidades do Cliente
- Visualização do cardápio
- Seleção de produtos e quantidades
- Cálculo automático do total
- Frete grátis para compras acima de R$ 80,00
- Contato via WhatsApp
- Links para redes sociais

## Estrutura do Projeto

```
projeto-hamburgueria/
├── hambug-venv/              # Ambiente virtual Python
├── hamburgueria/             # Projeto Django principal
│   ├── core/                 # App principal
│   │   ├── models.py         # Modelos do banco de dados
│   │   ├── views.py          # Views/Controllers
│   │   ├── forms.py          # Formulários
│   │   ├── consumers.py      # WebSocket consumers
│   │   ├── static/           # Arquivos estáticos (CSS, JS, imagens)
│   │   └── templates/        # Templates HTML
│   ├── hamburgueria/         # Configurações do Django
│   │   ├── settings.py       # Configurações
│   │   ├── urls.py           # URLs principais
│   │   └── asgi.py           # Configuração ASGI
│   ├── media/                # Upload de arquivos
│   ├── staticfiles/          # Arquivos estáticos coletados
│   ├── manage.py             # Script de gerenciamento Django
│   ├── package.json          # Dependências Node.js
│   └── webpack.config.js     # Configuração do Webpack
├── docs/
│   └── requirements.txt      # Dependências Python
└── images/                   # Imagens dos produtos
```

## Como Iniciar o Projeto

### Pré-requisitos
- Python 3.12 ou superior
- Node.js (para o Webpack)
- Redis Server (para WebSockets)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Erick-Bryan-Cubas/projeto-hamburgueria.git
   cd projeto-hamburgueria
   ```

2. **Ative o ambiente virtual:**
   ```bash
   # No Windows
   .\hambug-venv\Scripts\Activate.ps1
   # ou
   hambug-venv\Scripts\activate.bat
   
   # No Linux/Mac
   source hambug-venv/bin/activate
   ```

3. **Instale as dependências Python (se necessário):**
   ```bash
   pip install -r docs/requirements.txt
   ```

4. **Navegue para o diretório do Django:**
   ```bash
   cd hamburgueria
   ```

5. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Colete os arquivos estáticos:**
   ```bash
   python manage.py collectstatic
   ```

8. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

9. **Acesse o sistema:**
   - Aplicação principal: http://127.0.0.1:8000/
   - Admin Django: http://127.0.0.1:8000/admin/

### Configurações Adicionais

#### Redis (para WebSockets)
Certifique-se de que o Redis esteja rodando. O projeto está configurado para usar:
```
redis://:41X5FdKfcumkdjX@172.18.255.231:6379
```

#### Webpack (para desenvolvimento frontend)
Se precisar trabalhar com os assets frontend:
```bash
npm install
npm run dev  # ou npm run build para produção
```

## Regras de Negócio

- **Frete grátis** para compras acima de R$ 80,00
- **Frete fixo** de R$ 15,00 para compras abaixo de R$ 80,00
- Produtos com **desconto** são destacados na interface
- **Tempo de preparo** é calculado automaticamente
- Comunicação em **tempo real** via WebSockets

## Ambientes

### Desenvolvimento
- Debug habilitado
- SQLite como banco de dados
- Arquivos de mídia servidos pelo Django

### Produção
Configure as variáveis de ambiente no arquivo `.env`:
```env
DEBUG=False
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=seu-dominio.com
```

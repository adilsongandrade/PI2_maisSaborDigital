## 📝 Guia de Desenvolvimento Colaborativo - Mais Sabor Digital

O **Mais Sabor Digital** é um sistema web construído em **Django** para auxiliar empreendedores do ramo de alimentos na gestão de fichas técnicas, cálculo de custos, sugestão de preço mínimo, análise de dados, acessibilidade e gestão tributária.

Este guia detalha o processo de configuração do ambiente de desenvolvimento local, execução do projeto e contribuições para o repositório principal.

---

### 🚀 1. Visão Geral do Projeto

* **Tecnologias Principais:** Python 3.x, **Django 5.2.1**.
* **Banco de Dados:** MySQL (via Aiven/MySQL Connector).
* **Gestão de Dependências:** `pip` e ambiente virtual (`venv`).
* **Hospedagem (Deployment):** **Vercel** (CI/CD automatizado).
* **Estáticos:** `Whitenoise` para servir arquivos estáticos em produção.

---

### 💻 2. Configuração do Ambiente Local

Siga os passos abaixo para preparar seu ambiente de desenvolvimento.

#### 2.1. Pré-requisitos

Certifique-se de ter instalado em sua máquina:

1.  **Python 3.x** (Recomendado: 3.10 ou superior).
2.  **Git** (Para clonagem e versionamento).
3.  **Terminal/Linha de Comando** (Shell, PowerShell, Git Bash, etc.).

#### 2.2. Clonagem do Repositório

Abra seu terminal e execute os seguintes comandos:

```bash
# 1. Clone o projeto para sua máquina
git clone [https://github.com/adilsongandrade/PI2_maisSaborDigital.git](https://github.com/adilsongandrade/PI2_maisSaborDigital.git)

# 2. Acesse o diretório do projeto
cd PI2_maisSaborDigital
````

#### 2.3. Criação e Ativação do Ambiente Virtual

É crucial isolar as dependências do projeto.

```bash
# 1. Crie o ambiente virtual (O nome 'venv' é o padrão)
python -m venv venv

# 2. Ative o ambiente virtual

# No Windows (Prompt de Comando/PowerShell):
.\venv\Scripts\activate

# No Linux ou macOS (Terminal):
source venv/bin/activate
```

> **Nota:** Após a ativação, o nome `(venv)` aparecerá no início da sua linha de comando.

#### 2.4. Instalação de Dependências

Instale todas as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

-----

### ⚙️ 3. Configuração das Variáveis de Ambiente (`.env`)

O projeto usa variáveis de ambiente para dados sensíveis (`SECRET_KEY`, credenciais do banco).

1.  Crie um novo arquivo chamado **`.env`** na raiz do projeto (no mesmo nível do `manage.py`).
2.  Preencha-o com as seguintes variáveis. **Atenção: Use seus próprios valores seguros, especialmente para a `SECRET_KEY` e a senha do banco.**

<!-- end list -->

```dotenv
# .env - Variáveis de ambiente para o ambiente LOCAL
# ----------------------------------------------------

# Chave secreta do Django (Gerar uma string segura)
SECRET_KEY='sua-chave-secreta-aqui-gerada-localmente'

# Controle de debug
# Para ambiente local de desenvolvimento, é geralmente TRUE
DEBUG='True'

# Variáveis do Banco de Dados MySQL (Aiven)
# Use as credenciais fornecidas pela equipe ou pelo Aiven
DB_PASSWORD='sua-senha-do-banco-de-dados'
```

> **⚠️ Importante:** O arquivo **`.env`** **NÃO DEVE** ser enviado ao Git. Verifique se ele está listado no seu `.gitignore`.

-----

### 🗃️ 4. Configuração e Inicialização do Banco de Dados

O projeto está configurado para usar um banco de dados **MySQL** remoto (conforme `settings.py`).

1.  **Certifique-se de que sua máquina tem permissão** para se conectar ao host MySQL (`mysql-3faa46f0-...`).
2.  **Execute as Migrações** para criar as tabelas do Django no banco de dados configurado:

<!-- end list -->

```bash
# Aplica as migrações (cria as tabelas do 'core' e Django)
python manage.py migrate
```

3.  **Crie um Superusuário** (necessário para acessar a área `/admin`):

<!-- end list -->

```bash
python manage.py createsuperuser
```

-----

### ▶️ 5. Execução do Projeto

Com tudo configurado, você pode iniciar o servidor de desenvolvimento do Django.

```bash
python manage.py runserver
```

  * O projeto estará acessível em: **`http://127.0.0.1:8000/`**
  * O painel de administração estará em: **`http://127.0.0.1:8000/admin/`**

-----

### 🤝 6. Fluxo de Contribuição Colaborativa (Gitflow Simplificado)

Para garantir que o trabalho em equipe seja organizado e que o código principal (`main`) permaneça estável, todos os colaboradores devem seguir este fluxo:

#### 6.1. Sincronizar (Pull)

Sempre comece seu trabalho puxando as últimas alterações da *branch* principal:

```bash
# 1. Mude para a branch principal (main)
git checkout main

# 2. Baixe as últimas alterações
git pull origin main
```

#### 6.2. Criar uma *Feature Branch*

**Nunca** trabalhe diretamente na *branch* `main`. Crie uma *branch* específica para sua nova funcionalidade ou correção:

```bash
# Formato sugerido: 'feature/nome-da-funcionalidade' ou 'bugfix/nome-do-erro'
git checkout -b feature/minha-nova-funcionalidade
```

#### 6.3. Codificar e Testar Localmente

1.  Implemente suas alterações (código, templates, estáticos).
2.  **Execute o servidor (`python manage.py runserver`) e teste minuciosamente suas alterações localmente.**
3.  Execute quaisquer testes de unidade (se existirem): `python manage.py test`.

#### 6.4. Enviar as Alterações (Commit e Push)

Quando sua funcionalidade estiver pronta e testada:

```bash
# 1. Adicione os arquivos alterados
git add . 

# 2. Faça o commit com uma mensagem clara e descritiva
git commit -m "feat: Adiciona cálculo de impostos na ficha técnica"

# 3. Envie a branch para o GitHub
git push origin feature/minha-nova-funcionalidade
```

#### 6.5. Abrir um *Pull Request* (PR)

1.  Acesse o repositório no **GitHub**.
2.  Você verá uma notificação para criar um **Pull Request** da sua nova *branch* para a *branch* `main`.
3.  Preencha a descrição do PR, explicando o que foi feito.
4.  **Marque um colega de equipe para revisão (Code Review).**

-----

### 🌐 7. Deploy Automatizado (Vercel)

O *deployment* em produção é **automatizado**:

  * Qualquer **Merge** (fusão) aceito na *branch* **`main`** no GitHub dispara automaticamente um novo *build* e *deploy* na Vercel.
  * A equipe pode verificar o status do *deploy* no painel do Vercel ou no próprio GitHub.

-----

### 📚 8. Recursos Úteis

  * **Documentação Oficial do Django:** `https://docs.djangoproject.com/en/5.2/`
  * **Repositório do Projeto:** `https://github.com/adilsongandrade/PI2_maisSaborDigital`
  * **Aplicação em Produção (Vercel):** `https://pi-2-mais-sabor-digital.vercel.app`

<!-- end list -->

```
```

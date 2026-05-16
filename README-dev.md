# cristiano-22505051


# COMANDOS DJANGO IMPORTANTES

## Entrar no projeto

```bash
cd nome-do-projeto
```

## Criar ambiente virtual

```bash
python -m venv venv
```

## Ativar ambiente virtual

### Linux / Codespaces / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Instalar dependências do projeto

```bash
pip install -r requirements.txt
```

## Guardar dependências atuais

```bash
pip freeze > requirements.txt
```

## Ligar servidor Django

```bash
python manage.py runserver
```

ou

```bash
python manage.py runserver 0.0.0.0:8000
```

## Parar servidor

```bash
CTRL + C
```

## Criar migrations

```bash
python manage.py makemigrations
```

## Aplicar migrations

```bash
python manage.py migrate
```

## Criar superuser admin

```bash
python manage.py createsuperuser
```

## Abrir shell Django

```bash
python manage.py shell
```

## Recolher ficheiros estáticos

```bash
python manage.py collectstatic --noinput
```

## Ver packages instalados

```bash
pip list
```

## Instalar package novo

```bash
pip install nome-do-package
```

Exemplo:

```bash
pip install pillow
```

## Ver status do Git

```bash
git status
```

## Adicionar alterações Git

```bash
git add .
```

## Fazer commit

```bash
git commit -m "mensagem"
```

## Enviar para GitHub

```bash
git push
```

## Atualizar projeto do GitHub

```bash
git pull
```

## Clonar repositório

```bash
git clone URL_DO_REPOSITORIO
```

## Apagar cache Python

```bash
find . -name "__pycache__" -type d -exec rm -rf {} +
```

## Abrir admin Django

```text
/admin
```

## Abrir site local

```text
http://127.0.0.1:8000
```

## Estrutura importante Django

```text
templates/
static/
media/
models.py
views.py
urls.py
admin.py
forms.py
```

from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20)
    grau = models.CharField(max_length=50)
    departamento = models.CharField(max_length=150)
    descricao = models.TextField()
    duracao_anos = models.PositiveIntegerField()
    imagem = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    area_especializacao = models.CharField(max_length=150)
    pagina_pessoal_url = models.URLField(blank=True)
    foto = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    website_oficial = models.URLField(blank=True)
    logo = models.URLField(blank=True)
    nivel_proficiencia = models.CharField(max_length=50)
    nivel_interesse = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="tecnologias"
    )

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    nome = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    certificado_url = models.URLField(blank=True)

    tecnologias = models.ManyToManyField(
        Tecnologia,
        blank=True,
        related_name="formacoes"
    )
    competencias = models.ManyToManyField(
        Competencia,
        blank=True,
        related_name="formacoes"
    )

    def __str__(self):
        return self.nome


class TFC(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    ano = models.PositiveIntegerField()
    resumo = models.TextField()
    area_tematica = models.CharField(max_length=150)
    url_documento = models.URLField(blank=True)
    classificacao_interesse = models.CharField(max_length=50)

    tecnologias = models.ManyToManyField(
        Tecnologia,
        blank=True,
        related_name="tfcs"
    )
    competencias = models.ManyToManyField(
        Competencia,
        blank=True,
        related_name="tfcs"
    )

    def __str__(self):
        return self.titulo


class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    objetivos = models.TextField()
    conhecimentos_aplicados = models.TextField()
    github_url = models.URLField(blank=True)
    imagem = models.URLField(blank=True)
    estado = models.CharField(max_length=50)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="projetos"
    )
    tfcs = models.ManyToManyField(
        TFC,
        blank=True,
        related_name="projetos"
    )

    def __str__(self):
        return self.titulo


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20)
    ano_curricular = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.DecimalField(max_digits=4, decimal_places=1)
    descricao = models.TextField()
    imagem = models.URLField(blank=True)

    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name="unidades_curriculares"
    )
    docentes = models.ManyToManyField(
        Docente,
        blank=True,
        related_name="unidades_curriculares"
    )
    projetos = models.ManyToManyField(
        Projeto,
        blank=True,
        related_name="unidades_curriculares"
    )

    def __str__(self):
        return self.nome


class MakingOf(models.Model):
    titulo = models.CharField(max_length=150)
    entidade_alvo = models.CharField(max_length=150)
    erros_encontrados = models.TextField()
    correcoes_realizadas = models.TextField()
    justificacao_opcoes = models.TextField()
    uso_ia = models.TextField()
    contributo_ia = models.TextField()
    foto_der = models.ImageField(upload_to='makingof/der/', null=True, blank=True)
    data_registo = models.DateField()

    def __str__(self):
        return self.titulo



class FotoMakingOf(models.Model):
    making_of = models.ForeignKey(
        MakingOf,
        on_delete=models.CASCADE,
        related_name='fotos'
    )
    imagem = models.ImageField(upload_to='makingof/fotos/')

    def __str__(self):
        return f"Foto de {self.making_of.titulo}"

       
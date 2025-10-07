from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter
def slugify_filename(value):
    """
    Converte nomes de receitas em formato seguro (slug),
    removendo acentos, espaços e caracteres especiais.
    Exemplo: 'Batata Rústica' -> 'batata-rustica'
    """
    if not value:
        return ''
    return slugify(value)

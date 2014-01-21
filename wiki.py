from trytond.model import ModelView, ModelSQL, fields

#list of all classes in the file
__all__ = ['Wiki']


class Wiki(ModelSQL, ModelView):
    #description
    'Wiki'
    #Internal class name. Always used as a reference inside Tryton
    #default: <module name> + . + <class name> on Tryton
    #and on database <modules name> + _ + <class name>
    __name__ = 'wiki.wiki'
    article_name = fields.Char('Subject Article', required=True)
    content = fields.Char('Content', required=True)

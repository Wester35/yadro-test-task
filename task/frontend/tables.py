import django_tables2 as tables
from api.models import User

class UserTable(tables.Table):
    picture_thumbnail = tables.TemplateColumn('<img src="{{ record.picture_thumbnail }}" alt="thumbnail">')

    link = tables.TemplateColumn(
        '<a href="/{{ record.id }}/" class="btn btn-primary btn-sm">Перейти</a>',
        orderable=False,
        verbose_name='Link'
    )

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "gender", "name", "surname", "phone_number", "email", "picture_thumbnail", "location", "link")

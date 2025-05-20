import django_tables2 as tables
from api.models import User

class UserTable(tables.Table):
    picture_thumbnail = tables.TemplateColumn('<img src="{{ record.picture_thumbnail }}" alt="thumbnail">')

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "gender", "name", "surname", "phone_number", "email", "picture_thumbnail", "location", "link")

from .models import Category
def menu_links(request): #Is function ka main goal hai har template me Category ki links ko automatically accessible banana
    links = Category.objects.all()
    return dict(links=links)
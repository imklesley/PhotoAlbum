from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from photos.forms import AddPhoto
from photos.models import Photo, Category


def gallery(request):
    context = {}

    category = request.GET.get('category')
    if category == None:
        context['gallery'] = Photo.objects.all()
    else:
        #Para acessar um atributo de um atributo(no caso de um atributo que é uma chave estrangeira e possui sua própria
        # table, basta usar o nome do atributo__nomeAtributoDaTableEstrangeira)
        context['gallery'] = Photo.objects.filter(category__name=category)
        print(context['gallery'])
    context['categories'] = Category.objects.all()

    return render(request, 'photos/gallery.html', context)


def add_photo(request):
    context = {}

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print(data)
        print(image)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        photo = Photo(
            category=category,
            title=data['title'],
            description=data['description'],
            image=image,
        )

        photo.save()

        return redirect('gallery')

    else:
        context['categories'] = Category.objects.all()
        return render(request, 'photos/add.html', context)


def view_photo(request, id: int):
    context = {}

    context['photo'] = Photo.objects.get(id=id)

    return render(request, 'photos/photo.html', context)

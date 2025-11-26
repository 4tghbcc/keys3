from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import NameForm
from .models import UserName

def index(request):
    """Главная страница с формой ввода имени"""
    form = NameForm()
    
    # Получаем последние 5 имен для отображения
    recent_names = UserName.objects.all()[:5]
    
    context = {
        'form': form,
        'recent_names': recent_names,
    }
    return render(request, 'users/index.html', context)

def greeting(request):
    """Обработка формы и отображение приветствия"""
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            try:
                # Сохраняем имя в базе данных
                user_name = form.save()
                
                # Создаем персонализированное приветствие
                context = {
                    'name': user_name.name,
                    'total_users': UserName.objects.count()
                }
                return render(request, 'users/greeting.html', context)
                
            except Exception as e:
                messages.error(request, f'Произошла ошибка при сохранении: {str(e)}')
                return redirect('index')
        else:
            # Если форма невалидна, показываем ошибки
            for error in form.errors.values():
                messages.error(request, error)
            return redirect('index')
    
    # Если метод не POST, перенаправляем на главную
    return redirect('index')

def name_list(request):
    """Страница со списком всех имен"""
    names = UserName.objects.all().order_by('-created_at')
    context = {
        'names': names,
        'total_count': names.count()
    }
    return render(request, 'users/name_list.html', context)

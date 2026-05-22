# portfolio/views.py
from django.shortcuts import render, redirect

def home(request):
    lang = request.session.get('lang', 'vi')
    if lang not in ['vi', 'en']:
        lang = 'vi'

    # Chỉ truyền trạng thái ngôn ngữ sang trang chủ HTML
    return render(request, 'home.html', {'current_lang': lang})

def skill_detail(request, num):
    lang = request.session.get('lang', 'vi')
    if lang not in ['vi', 'en']:
        lang = 'vi'

    # Tự động gọi file HTML tĩnh tương ứng (skill_detail_1.html, skill_detail_2.html...)
    template_name = f'skill/skill_detail_{num}.html'
    
    return render(request, template_name, {'current_lang': lang})

def change_lang(request, lang_code):
    if lang_code in ['vi', 'en']:
        request.session['lang'] = lang_code
    return redirect(request.META.get('HTTP_REFERER', '/'))
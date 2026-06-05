# portfolio/views.py
from django.shortcuts import render, redirect
from .models import PageView
import requests
from django.shortcuts import render
from .models import AccessLog  # Import model mới vào đây

def get_client_ip(request):
    """Hàm bổ trợ lấy địa chỉ IP thật của người dùng"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    # 1. Xử lý logic ngôn ngữ hiện tại của bạn
    lang = request.session.get('lang', 'vi')
    if lang not in ['vi', 'en']:
        lang = 'vi'

    # 2. Lấy IP và định vị bằng ip-api.com
    user_ip = get_client_ip(request)
    
    # Mẹo test dưới localhost (vì 127.0.0.1 không định vị được địa lý công cộng)
    # Nếu chạy local, hệ thống sẽ tự dùng IP mẫu ở Đà Nẵng để bạn test thử dữ liệu đầu ra
    if user_ip in ['127.0.0.1', 'localhost']:
        user_ip = '113.176.96.0' 

    # Các giá trị mặc định nếu API lỗi hoặc không tìm thấy
    country = 'Không rõ'
    region = 'Không rõ'
    isp = 'Không rõ'

    try:
        # Gọi API lấy thông tin quốc gia, tỉnh/thành, nhà mạng (giới hạn timeout 3s để tránh nghẽn trang)
        response = requests.get(f'http://ip-api.com/json/{user_ip}?fields=status,country,regionName,isp', timeout=3)
        data = response.json()
        
        if data.get('status') == 'success':
            country = data.get('country', 'Không rõ')
            region = data.get('regionName', 'Không rõ')
            isp = data.get('isp', 'Không rõ')
    except Exception as e:
        # Ghi log lỗi ra terminal nếu API gặp sự cố, tránh làm sập trang web của bạn
        print(f"Lỗi gọi API định vị: {e}")

    # 3. Lưu thông tin chi tiết vào database (Mỗi lần vào trang là 1 dòng log mới)
    AccessLog.objects.create(
        page_name='home',
        ip_address=user_ip,
        country=country,
        region=region,
        isp=isp
    )

    view_obj, created = PageView.objects.get_or_create(page_name='home')
    # Tăng số lượt truy cập và lưu lại
    view_obj.count += 1
    view_obj.save()

    # 4. Đếm tổng số lượt truy cập của trang 'home' từ trước tới nay để hiển thị ra giao diện
    total_views = PageView.objects.get(page_name='home').count

    # 5. Truyền dữ liệu sang template HTML của bạn
    return render(request, 'home.html', {
        'current_lang': lang, 
        'page_view': total_views
    })
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


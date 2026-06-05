# portfolio/models.py
from django.db import models
from django.urls import reverse

class PageView(models.Model):
    # Định danh tên trang (ví dụ: 'home', 'skill_detail_1')
    page_name = models.CharField(max_length=100, unique=True)
    # Số lượng truy cập
    count = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.page_name}: {self.count} views"
    
class AccessLog(models.Model):
    page_name = models.CharField(max_length=100, default='home')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    country = models.CharField(max_length=100, default='Không rõ')
    region = models.CharField(max_length=100, default='Không rõ') # Tỉnh/Thành phố
    isp = models.CharField(max_length=255, default='Không rõ')    # Nhà mạng
    accessed_at = models.DateTimeField(auto_now_add=True)         # Thời gian truy cập

    def __str__(self):
        return f"{self.page_name} - {self.region}, {self.country} ({self.accessed_at})"
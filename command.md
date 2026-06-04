# hướng dẫn push lên github mỗi lần sửa đổi
git add .
git commit -m "hoàn thiện tạm thời còn skill 5 chưa có sơ đồ mối sửa lại mail và chỗ tải cv"
git push origin main

### mỗi lần sửa đổi ở trên pythonanywhere
source /home/dungwork/.virtualenvs/myenv/bin/activate
cd My-porfolio
git pull origin main

# Cách xem các phiên bản trước đó tư cũ nhất tới mới nhất để thực hiện việc back version
git log --oneline --reverse
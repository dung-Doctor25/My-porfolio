# hướng dẫn push lên github mỗi lần sửa đổi
git add .
git commit -m "cập nhật LẠI LINK CV"
git push origin main

### mỗi lần sửa đổi ở trên pythonanywhere
source /home/dungwork/.virtualenvs/myenv/bin/activate
cd My-porfolio
git pull origin main

# Cách xem các phiên bản trước đó tư cũ nhất tới mới nhất để thực hiện việc back version
git log --oneline --reverse
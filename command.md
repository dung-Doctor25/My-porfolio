# hướng dẫn push lên github mỗi lần sửa đổi
git add .
git commit -m "bản hoàn thành skill 1( cần bổ sung wh, cloud),2 (có thể nói là xong),3( xong chưa biết bổ sung không)"
git push origin main

### mỗi lần sửa đổi ở trên pythonanywhere
source /home/dungwork/.virtualenvs/myenv/bin/activate
cd My-porfolio
git pull origin main

# Cách xem các phiên bản trước đó tư cũ nhất tới mới nhất để thực hiện việc back version
git log --oneline --reverse
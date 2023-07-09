# 使用官方 Python 基礎映像
FROM python:3.7

# 設定工作目錄
WORKDIR /app

# 複製 requirements.txt 到容器中
COPY requirements.txt .

# 安裝依賴套件
RUN pip install -r requirements.txt

# 複製整個專案到容器中
COPY . .

# 開放對外的埠號
EXPOSE 8000

# 啟動 Django 開發伺服器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

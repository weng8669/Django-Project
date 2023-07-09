## Django-Project
執行以下指令建立 Docker 映像：

docker-compose build

執行以下指令啟動 Django 開發伺服器：

docker-compose up

透過 http://localhost:8000/articles/ 存取文章 API，並使用 JWT Token 進行身份驗證。


建立資料庫遷移檔案：

docker-compose run web python manage.py makemigrations

執行資料庫遷移：

docker-compose run web python manage.py migrate

建立測試資料：

docker-compose run web python manage.py shell

在 Django shell 中，執行以下程式碼：

from myproject.models import Article

建立測試資料:

Article.objects.create(title='文章標題', author='作者', content='文章內容', image='https://example.com/image1.jpg')

## 透過 API 存取文章資料。以下是範例請求：

取得所有文章：GET http://localhost:8000/articles/

取得單一文章：GET http://localhost:8000/articles/<article_id>/

新增文章：POST http://localhost:8000/articles/

更新文章：PUT http://localhost:8000/articles/<article_id>/

刪除文章：DELETE http://localhost:8000/articles/<article_id>/

<article_id> 是指文章的 ID，可以從取得文章列表中的回應中找到相應的 ID。

## 建立一個使用者帳號，並產生 JWT Token。

docker-compose run web python manage.py createsuperuser

按照提示提供使用者名稱和密碼，並建立一個超級使用者帳號。

使用這個使用者帳號來取得 JWT Token

docker-compose run web python manage.py drf_create_token (username)

將username替換為你剛建立的使用者名稱。這將產生一個 JWT Token，使用它來透過 API 操作文章。

使用超級使用者帳號來取得 JWT Token。請使用以下請求來獲取 Token：

curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"your-username\", \"password\": \"your-password\"}" http://localhost:8000/api/token/

將your-username和your-password替換為剛建立的超級使用者帳號的使用者名稱和密碼。

成功請求後，你會收到一個回應，其中包含 access 和 refresh 的 JWT Token。你可以使用 access Token 來進行 API 操作。

curl -X GET -H "Authorization: Bearer <access-token>" http://localhost:8000/articles/

將access-token替換為你獲得的access Token。

就可以透過 JWT Token 進行身份驗證並操作「熱門文章」 API。

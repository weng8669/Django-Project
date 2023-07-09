import jwt

def generate_jwt_token(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxfQ.VWEPoFGPKV8q5vcQefQy28zhVeLUZmjSj5SGoD1VQJI', algorithm='HS256')
    return token

# 使用範例
token = generate_jwt_token(1)
print(token)

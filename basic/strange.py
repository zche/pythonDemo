cors_origins = 'www.baidu.com'
result1 = cors_origins if cors_origins else ["*"]
print(result1)
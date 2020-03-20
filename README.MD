## 正正的运行需要配置代理 我用nginx

[转载教程](https://blog.csdn.net/FungLeo/article/details/80690367)

```sh
vim /etc/nginx/nginx.conf

server {
  server_name __YOU_DOMAIN_IN_HERE__;
  location / {
    proxy_pass  http://127.0.0.1:8000;
  }
}
```
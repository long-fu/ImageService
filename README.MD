## 正正的运行需要配置代理 我用nginx

```sh
vim /etc/nginx/nginx.conf

server {
  server_name __YOU_DOMAIN_IN_HERE__;
  location / {
    proxy_pass  http://127.0.0.1:8000;
  }
}
```
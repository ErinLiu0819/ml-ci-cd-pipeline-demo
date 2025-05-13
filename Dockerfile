FROM --platform=linux/amd64 python:3.9-slim
WORKDIR /app

# 先复制所有文件到容器中
COPY . .

# 安装依赖并运行训练脚本
RUN pip install --no-cache-dir -r requirements.txt && \
    python train.py

# 启动API服务
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
FROM node:20-slim

# 日本語フォントをインストール
RUN apt-get update && apt-get install -y fonts-noto sudo curl
# 必要なライブラリをインストール
RUN apt-get install -y \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgtk2.0-dev \
    libatk1.0-dev \
    libcairo2-dev \
    libfreetype6-dev \
    libncurses-dev \
    libsm-dev \
    libice-dev \
    libxi-dev \
    libxtst-dev \
    libgl1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libnss3-dev \
    libgdk-pixbuf2.0-dev \
    libgtk-3-dev \
    libxss-dev \
    libasound2
# 不要なキャッシュを削除
RUN rm -rf /var/lib/apt/lists/*

# node ユーザーに sudo 権限を付与
COPY sudoers.d/node /etc/sudoers.d/node

# node ユーザーに切り替え
USER node

# アプリケーションのソースコードをコンテナにコピー
COPY --chown=node:node . /workspaces

# 作業ディレクトリをアプリケーションディレクトリに設定
WORKDIR /workspaces

# Markdown PDFを少し改造した拡張機能を追加
COPY --chown=node:node local-extensions/yzane.markdown-pdf /home/node/.vscode-server/extensions/yzane.markdown-pdf
# 拡張機能のインストール
RUN npm ci --prefix /home/node/.vscode-server/extensions/yzane.markdown-pdf

# md-to-pdfをインストール
RUN npm ci

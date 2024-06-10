# AUTO_ANDROID

スマホゲーを全自動化するためのテンプレートレポジトリ

## howto

1. scrcpy をダウンロードしてくる

   > https://github.com/Genymobile/scrcpy

2. scrcpy をインストールしたディレクトリを、`common/CONST.py`に記述する

   ```
   SCRCPY_PATH = "/path/to/scrcpy/"
   ```

3. android デバイスの開発者オプションを有効にする

4. モジュールのインストール

   ```
   pip install -r requirements.txt
   ```

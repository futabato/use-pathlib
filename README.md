# pathlibを使おう

Pythonの標準ライブラリである`pathlib`を使用して、ファイルパス操作をより安全かつ直感的に行う方法を学ぶための資料です。

詳細は[公式ドキュメント](https://docs.python.org/ja/3.13/library/pathlib.html)をご覧ください。

## 使用方法

1. Dockerイメージをビルド

   ```bash
   $ docker image build -t python-alpine .
   ```

2. コンテナを実行

   ```bash
   $ docker container run --rm python-alpine
   ```

3. ruff によるチェック

   ```
   $ docker container run --rm python-alpine ruff check --select PTH .
   ```
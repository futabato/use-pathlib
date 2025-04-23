---
theme: "serif"
transition: "convex"
highlightTheme: "monokai"
---

2025/04/23

# Pathlibを使おう

---

本稿では、Pythonに標準で組み込まれているpathlibについて紹介します。

[pathlib --- オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3.13/library/pathlib.html)

---

普段からpathlib使っている人～～～～？

--

使っている人は偉いです。

特に新しいこともないので、このままpathlibを使っていきましょう。

--

pathlib使っていない人！！

os モジュール でファイルパス操作していますよね。

```python
>>> import os
>>> os.path.join('hoge', 'fuga')
>>> hoge/fuga
```

---

Pythonでは、標準でファイルを操作するための、
os モジュールが提供されています。

os モジュールの特徴

- 文字列操作ベースに記述する
- 記述量が多い
- やや可読性が低い
- ミスが起こりやすい問題

--

## pathlibの概要

pathlibは、ファイルやディレクトリのパス操作をオブジェクト指向で扱うことのできる、Python3.4から導入された標準ライブラリです。

`pathlib.Path` クラスを使用すると、ファイルやディレクトリのパスをオブジェクトとして操作できるため、より直感的で可読性の高いコードを書くことが可能になりました。

---

## os.path との違い

pathlib はオブジェクト指向であるため、`Path`オブジェクトに対してメソッドを呼び出すことで、ファイル操作を可能にします。

特に、`/` でパスの結合が表現できるのが強力です。最初は慣れないかもしれませんが、慣れるともう戻れません。

--

<style>
table {
  font-size: 0.6em;
}
</style>

| 機能 | os.path での書き方 | pathlib での書き方 |
| :-: | :-: | :-: |
| パスの結合 | `os.path.join(dir, file)` | `Path(dir) / file` |
| 絶対パスの取得 | `os.path.abspath(file)` | `Path(file).resolve()` |
| 拡張子の取得 | `os.path.splitext(file)[1]` | `Path(file).suffix` |
| ホームディレクトリのパスの取得 | `os.path.expanduser('~')` | `Path.home()` |
| 親ディレクトリの取得 | `os.path.dirname(file)` | `Path(file).parent` |
| ファイルが存在するか | `os.path.exists(file)` | `Path(file).exists()` |
| ファイルであるか | `os.path.isfile(file)` | `Path(file).is_file()` |
| ディレクトリであるか | `os.path.isdir(file)` | `Path(file).is_dir()` |

--

例えば`os.path`では、

 `os.path.join('hoge', 'fuga')` と実行すれば、`hoge/fuga` というパスが生成されます。

```python

>>> os.path.join('hoge', 'fuga')
'hoge/fuga'
```

--

簡単にパスが作れて便利！
ですが、

`os.path` には**引数が絶対パスであるとその前の引数は無視される**という仕様があります。

[os.path — Common pathname manipulations — Python 3.13.3 documentation](https://docs.python.org/ja/3.13/library/os.path.html#os.path.join)

--

例えば、引数の `hoga` に `/fuga` を与えると、`hoge` は無視され、`/fuga` というパスが生成されます。

```python
>>> import os
>>> os.path.join('hoge', '/fuga')
'/fuga'
```

--

3つ以上の引数を与える場合も同様に、絶対パスが含まれる前までの引数は無視されて結合されます。

```jsx
>>> os.path.join('/hoge', 'fuga', 'piyo')
'/hoge/fuga/piyo'
>>> os.path.join('hoge', 'fuga', '/piyo')
'/piyo'
>>> os.path.join('/hoge', 'fuga', '/piyo')
'/piyo'
>>> os.path.join('hoge', '/fuga', '/piyo')
'/piyo'
>>> os.path.join('/hoge', '/fuga', '/piyo')
'/piyo'
>>> os.path.join('/hoge', '/fuga', '/')
'/'
```

--

結構怖くないですか？

---

# DEMO

<https://github.com/futabato/use-pathlib>

--

```shell
git clone https://github.com/futabato/use-pathlib
docker image build -t python-alpine .
```

```
docker container run --rm python-alpine
```

---

## `Path` の基本的な使い方

--

### パスの作成

```python
from pathlib import Path

p = Path("/home/user/file.txt")
print(type(p), p)
```

↓

```text
<class 'pathlib._local.PosixPath'> /home/user/file.txt
```

--

### パスの結合

```python
p = Path("/home/user/desktop") / "file.txt"
print(p)
```

↓

```text
/home/user/desktop/file.txt
```

--

### 絶対パスの取得

```python
p = Path("file.txt").resolve()
print(p)  # file.txtまでの絶対パスが表示される
```

↓

```text
/home/user/ghq/github.com/futabato/use-pathlib/file.txt
```

--

### **パスの属性を取得**

```python
p = Path("/home/user/desktop/file.txt")

print(p.name)       # ファイル名 -> `file.txt`
print(p.stem)       # 拡張子なしのファイル名 -> `file`
print(p.suffix)     # 拡張子 -> `.txt`
print(p.parent)     # 親ディレクトリ -> `/home/user/desktop`
print(p.exists())   # ファイルが存在するか -> `True`
print(p.is_dir())   # ディレクトリか？ -> `False`
print(p.is_file())  # ファイルか？ -> `True`
```

--

### ディレクトリの作成

```python
>>> p = Path.cwd() / 'test_dir'
>>> p.is_dir()
False
>>> p.mkdir(parents=True, exist_ok=True) # ディレクトリ作成, parents:
>>> p.is_dir()
True
>>>
```

引数 `parents` ：中間のディレクトリも作成する

--

### ファイルの削除

```python
p = Path("test.txt")
p.touch()  # 空のファイルを作成
p.unlink()  # ファイルを削除
```

--

### ディレクトリの削除

`Path.rmdir()` が削除できるのは、空のディレクトリの場合のみ。

空でないディレクトリを削除するには、`shutil.rmtree()` を使用する。

--

### ファイル一覧の取得

`Path.glob()` で正規表現を記述して、マッチするファイルの一覧を取得できる。

```python
p = Path("/home/user/desktop")
for file in p.glob("*.txt"): # すべての .txt ファイルを取得
    print(file)  
```

--

### ファイルの読み書き

```python
>>> p = Path.cwd() / "test.txt"
>>> p.touch()
>>> p.write_text("Hello, from pathlib!")
20
>>> print(p.read_text())
Hello, from pathlib!
>>>
```

---

## OS間の差異の吸収

クロスプラットフォーム対応する機会はあまりないとは思いますが、pathlib は OS の違いを意識せずに使えます。

`Path` はデフォルトで OS に応じたパス区切り (`\` や `/`) を処理してくれるので、OS に依存しないコードを書けます。
（osモジュールでやろうとすると結構地獄）

--

実行中のプラットフォームの判定は、以下のような条件分岐を使うとよいでしょう。

[platform ---  実行中プラットフォームの固有情報を参照する](https://docs.python.org/ja/3.13/library/platform.html)

```python
import platform

system = platform.system()

if system == "Windows":
    print("Windows環境")
elif system == "Linux":
    print("Linux環境")
elif system == "Darwin":
    print("macOS環境")
```

---

# Pathlibを使わせよう

--

Ruffやflake8 には、Pathlibが使われているか（osモジュールが使われていないか）をチェックするルールが存在します。

[Rules flake8-use-pathlib (PTH)| Ruff](https://docs.astral.sh/ruff/rules/#flake8-use-pathlib-pth)

--

```
docker container run --rm python-alpine ruff check --select PTH
```

---

END
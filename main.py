import os

# /workspace/log と /log ディレクトリを作成
os.makedirs('/workspace/log', exist_ok=True)
os.makedirs('/log', exist_ok=True)

print("ルートディレクトリの内容：")
print(os.listdir('/'), end='\n\n')

# os.path.join の仕様により誤ってディレクトリを削除してしまうシナリオ
# /workspace/log を削除しようとするが、誤ってルートの /log が削除される
print("削除したいパス: /workspace/log", end='\n\n')
delete_path = os.path.join('/workspace', '/log')  # 引数が絶対パスであるとその前の引数は無視される
print(f"削除されるパス: {delete_path}", end='\n\n')

os.rmdir(delete_path)  # /logが削除される（/workspace/logではなくルートの /log）

# /log が削除されたか確認
print("ルートディレクトリの内容：")
print(os.listdir('/'))
if not os.path.exists('/log'):
    print("/log ディレクトリが削除されてしまいました！")
else:
    print("/log ディレクトリはまだ存在します。")

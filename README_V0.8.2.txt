ProductSiteCMS V0.8.2

【今回の修正】
V0.8.1のstart_api.batはUTF-8の日本語を含んでおり、
Windows 7のコマンドプロンプトで文字列の一部が
コマンドとして誤認識される場合がありました。

V0.8.2では次のように変更しています。

・start_api.batをASCII文字だけで作成
・改行コードをWindows用CRLFへ変更
・chcp 65001を廃止
・Python 3.8の代表的な保存場所を自動検索
・起動したPythonの場所とバージョンを表示
・エラー時に画面を閉じず、内容を確認可能
・API接続確認用BATを追加
・Pythonパス手動指定版BATも追加

【上書き先】
V0.8.2フォルダの中身を次へ上書きしてください。

C:\inetpub\wwwroot\

【起動】
Win7で次をダブルクリックします。

C:\inetpub\wwwroot\server\start_api.bat

正常時は次のような表示になります。

ProductSiteCMS V0.8.2 API Launcher
Python:
C:\...\python.exe
Python 3.8.x
Starting API on port 8765...

続いてAPI本体の表示が出ます。

ProductSiteCMS V0.8.2 保存API
URL : http://0.0.0.0:8765/api/status

この黒い画面は閉じずに使用してください。

【接続確認】
APIを起動した状態で、Win7のブラウザから次を開きます。

http://127.0.0.1:8765/api/status

正常ならJSONが表示されます。

または次をダブルクリックします。

C:\inetpub\wwwroot\server\test_api_connection.bat

【自動検出で起動しない場合】
次のファイルを右クリックして編集します。

C:\inetpub\wwwroot\server\start_api_manual_path.bat

この行を実際のPython 3.8の場所へ変更します。

set "PYTHON_EXE=C:\Python38\python.exe"

Pythonの場所はコマンドプロンプトで次を実行すると確認できます。

where python

【CMS側】
API接続後、管理画面をCtrl+F5で再読み込みします。

http://192.168.11.17/admin/

上部表示が次になれば成功です。

● Win7 API接続中

その後、

サーバーへ保存

を押すと画像・games.json・products.jsonがWin7へ直接保存されます。

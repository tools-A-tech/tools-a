ProductSiteCMS V0.8

【V0.8の追加機能】
・ゲームタイトル自体を削除
・タイトル削除時、紐づく商品もまとめて削除
・画像をWin7のimagesフォルダへ直接アップロード
・games.jsonとproducts.jsonをWin7へ直接保存
・保存前JSONの自動バックアップ
・管理画面上部にAPI接続状態を表示
・手動ダウンロード保存は予備機能として残しています

【設置】
V0.8フォルダの中身を次へ上書きします。

C:\inetpub\wwwroot\

【保存APIの起動】
Win7で次をダブルクリックします。

C:\inetpub\wwwroot\server\start_api.bat

黒い画面は閉じずに起動しておいてください。

管理画面:
http://192.168.11.17/admin/

管理画面上部が次の表示になれば接続成功です。

● Win7 API接続中

【編集から公開サイト反映まで】
1. 商品・タイトルを追加、編集、削除
2. 画像をドラッグ＆ドロップ
3. 画面上部の「サーバーへ保存」
4. 公開サイトを再読み込み

次へ直接保存されます。

C:\inetpub\wwwroot\data\games.json
C:\inetpub\wwwroot\data\products.json
C:\inetpub\wwwroot\images\

画像を手作業でimagesへコピーする必要はありません。

【画像アップロード】
「画像アップロード」は画像だけ先に保存したい場合に使います。
通常は「サーバーへ保存」だけで、未アップロード画像も先に保存されます。

【タイトル削除】
ゲームタイトルを開き、商品一覧の一番下にある

このタイトルを削除

を押します。

対象タイトルと、そのタイトルに紐づく全商品が削除対象になります。
最後に「サーバーへ保存」を押すと実ファイルへ反映されます。

【バックアップ】
サーバーへ保存するたび、変更前のJSONが次へ保存されます。

C:\inetpub\wwwroot\data\backups\

【API未接続の場合】
・start_api.batが起動しているか確認
・WindowsファイアウォールでPythonの通信を許可
・Python 3.8がインストールされているか確認
・必要な場合はstart_api.batを右クリックし「管理者として実行」

【現時点の公開範囲】
V0.8はWin7 IIS上の公開サイトへ直接反映する段階です。
GitHub Pagesへのgit add / commit / push自動化は次工程です。

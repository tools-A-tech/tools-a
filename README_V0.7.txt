ProductSiteCMS V0.7

【追加機能】
・アイコン画像をドラッグ＆ドロップ
・クリックしてフォルダから画像選択
・PNG / JPG / JPEG / WebP対応
・最大5MB
・画像プレビュー
・ファイル名と容量表示
・画像ファイル名を自動整形
・games.jsonへ images/ファイル名 を自動登録
・タイトル追加時に画像ファイルもダウンロード
・既存画像パスの直接入力も可能

【管理画面】
http://192.168.11.17/admin/

【使用手順】
1. ページ最下部の「＋ 新規タイトルを追加」
2. 画像を枠へドラッグ＆ドロップ、または枠をクリック
3. タイトル・商品情報を入力
4. 「タイトル・商品・画像を追加」
5. 保存された画像を次へコピー
   C:\inetpub\wwwroot\images\
6. games.json と products.json を保存
7. 次へ上書き
   C:\inetpub\wwwroot\data\games.json
   C:\inetpub\wwwroot\data\products.json

【注意】
ブラウザの安全制限により、V0.7では画像をIISフォルダへ直接書き込めません。
画像ファイルは自動ダウンロードされ、games.json側の画像パスは自動設定されます。

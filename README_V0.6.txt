ProductSiteCMS V0.6

【V0.6の追加機能】
・公開サイトと同じデザインの編集画面を継続
・既存商品ポップアップから商品の編集
・商品一覧最下部から新規商品追加
・サイト下部に「＋ 新規タイトルを追加」を追加
・ゲームタイトルと最初の商品を同時登録
・新規categoryを自動発行
・ゲームID、商品ID、並び順を自動設定
・アイコン画像URLまたは画像パスを設定
・アイコンプレビュー
・タイトル、価格、商品説明、販売状態を入力
・追加した商品にX・LINE連絡ボタンを自動表示
・products.json保存
・games.json保存

【管理画面URL】
http://192.168.11.17/admin/

【公開サイトURL】
http://192.168.11.17/

GitHub Pagesを含め公開URLに変更はありません。

【Win7 IISへの設置】
V0.6フォルダの中身を以下へ上書きしてください。

C:\inetpub\wwwroot\

主な更新ファイル:
C:\inetpub\wwwroot\admin\index.html
C:\inetpub\wwwroot\admin\admin-data-loader.js

【新規タイトル追加手順】
1. http://192.168.11.17/admin/ を開く
2. ページ最下部の「＋ 新規タイトルを追加」
3. ゲームタイトルを入力
4. アイコン画像URLまたは images/... のパスを入力
5. 最初の商品タイトル、価格、商品説明を入力
6. 「タイトルと商品を追加」
7. 追加された商品ポップアップを確認
8. 上部の「games.json保存」
9. 上部の「products.json保存」
10. ダウンロードした2ファイルを以下へ上書き

C:\inetpub\wwwroot\data\games.json
C:\inetpub\wwwroot\data\products.json

【アイコン画像について】
画像ファイル自体を登録する場合は、画像を先に例えば以下へコピーします。

C:\inetpub\wwwroot\images\newgame.png

管理画面のアイコン欄には次を入力します。

images/newgame.png

【連絡ボタン】
新規商品には入力不要で、既存のsiteinfo.jsonに登録されているXとLINEのURLを自動使用します。

【現在の保存方式】
V0.6ではブラウザからJSONファイルを保存します。
管理画面からIIS上のJSONへ直接書き込む機能は、サーバー側保存APIを追加する次工程で実装します。

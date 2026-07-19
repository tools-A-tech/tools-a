ProductSiteCMS V1.1
GitHub連携・再実行対応版

接続先:
https://github.com/tools-A-tech/tools-a

【今回の状態から進める場合】
現在は以下まで完了しています。

・Git導入
・safe.directory登録
・origin登録
・git fetch
・mainブランチ作成
・origin/mainへのreset

V1.1を上書き後、APIの黒い画面を閉じて、
次を右クリックし「管理者として実行」してください。

C:\inetpub\wwwroot\server\finish_current_github_setup.bat

これは現在のCMSファイルをcommitし、GitHubへpushします。

【完全な初期設定をやり直す場合】
次を右クリックし「管理者として実行」します。

C:\inetpub\wwwroot\server\setup_github_connection.bat

V1.1では次を自動処理します。

・管理者権限確認
・Git確認
・safe.directory登録
・重複しないバックアップ作成
・Git初期化
・origin追加または修正
・fetch
・main/master判定
・checkout
・reset
・CMS復元
・commit
・push

途中で止まっても再実行できます。

【成功後】
APIを再起動します。

C:\inetpub\wwwroot\server\start_api.bat

Win11から管理画面を開き、Ctrl+F5を押します。

http://192.168.11.17/admin/

次の表示なら完成です。

● Win7 API接続中
● GitHub接続準備済み (main)

以後は管理画面の

保存してGitHub公開

だけで、Win7保存とGitHub Pages公開を行います。

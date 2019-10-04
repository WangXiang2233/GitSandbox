# ローカルリポジトリの作成

##  初期化して、現在あるファイルを追加して、コミットすればOK

ファイルがなければgit initのみでOK

> git init

> git add *

> git commit -m "initial commit"

## リモートリポジトリからプロジェクトをコピー

ターミナルでローカルリポジトリに移動して以下のコマンド

> cd [ローカルリポジトリのパス]

> git clone [リモートリポジトリパス] (例： https://github.com/jquery/jquery.git)

# ファイル更新までの基本手順

## ざっくりは以下の様な流れ

### ファイルを追加
### ファイルをコミット
### ファイルを更新

> git add [ファイル名] //追加

> git commit -a -m "任意のコメント"  //コミット (-aオプションは変更を自動検出してくれる)

> git push origin master  //masterを更新

#### git addの使用例

> git add . //すべてのファイル・ディレクトリ

> git add *.css //すべてのCSSファイル

> git add -n //追加されるファイルを調べる

> git add -u //変更されたファイルを追加する

> git rm --cached //addしてしまったファイルを除外

#### git commitの使用例

> git commit -a //変更のあったファイルすべて

> git commit --amend //直前のコミットを取り消す

> git commit -v //変更点を表示してコミット

#### コミットの取り消し

> git reset --soft HEAD~2 // 最新のコミットから2件分をワークディレクトリの内容を保持し取り消す

> git reset --hard HEAD~2 // 最新のコミットから2件分のワークディレクトリの内容とコミットを取り消す

#### コミットメッセージの修正

> git rebase -i HEAD~2 // HEADから2件のコミットメッセージ

上記のコマンドを実行するとVimが起動し、最新から過去2件のコミットが表示されます。

> pick {commit_id} {commit_meessage} // 2件目

> pick {commit_id} {commit_meessage} // 1件目(最新コミット)

pickの部分をeditもしくはeに変更後ファイルを保存し、修正が完了したら--amendオプションを付けてコミットする。

> git commit --amend

#### 最後に下記のコマンドを実行し完了。

> git rebase --continue

## ブランチの作成/移動/削除/変更/一覧/
## ブランチは変更履歴を記録できる。

> git branch [branch_name]  //ブランチの作成

> git checkout [branch_name]  //ブランチの移動

> git branch -d [branch_name]  //ブランチの削除

> git branch -m [branch_name]  //現在のブランチ名の変更

> git branch // ローカルブランチの一覧

> git branch -a //リモートとローカルのブランチの一覧

> git branch -r //リモートブランチの一覧

> git checkout -b branch_name origin/branch_name //リモートブランチへチェックアウト

# 編集をマージ

## master以外のブランチで編集した箇所をmasterに反映させる

> git checkout [branch_name]  //ブランチに移動

> git commit -a -m "コメント"  //変更ファイルをコミット

> git checkout master  //masterに移動

> git merge [branch_name]  //差分をマージ

> git push origin master  //ファイルの更新

## マージを取り消す

### コンフリクトが発生して一旦戻したい場合

> git merge --abort

### 差分を確認する

> git diff

> git diff HEAD^ //最後のコミットからの差分を表示

> git diff --name-only HEAD^ //差分ファイルを表示

> git diff file1.txt file2.txt //特定フィイルの差分

> git diff commit1 commit2 //コミットの差分

## ログの表示

> git log //コミットのログが見れる

> git reflog //いろいろ見れる

> git reflog origin/branch_name //pushのログが見れる

## ログには色々なオプションがあるけど、おすすめは以下のコマンド。

> git log --graph --name-status --pretty=format:"%C(red)%h %C(green)%an %Creset%s %C(yellow)%d%Creset"

# ファイルの名前変更

> git mv [変更前のファイル名] [変更後のファイル名]

> git commit -a -m "rename"

> git push origin master

# 特定ファイルを特定のコミットに戻す

## 特定のコミットに戻してmasterに反映したい場合は以下のコマンドで。

> git checkout [commit_id] [file_name]  //特定ファイルの指定

> git commit -a -m "return" //戻した内容をコミット

> git push origin master //変更をプッシュ

# 今やってる作業を一時退避する

> git stash

> git stash pop //戻す場合

> git stash list //退避の一覧

> git stash clear //退避の消去

# タグ

> git tag // タグの一覧表示

> git tag -l 'v1.*' // パターンでタグを検索

> git tag -a v0.0.0 -m 'version 0.0.0' // タグの作成

> git push origin v0.0.0 // タグの共有

# ファイルの削除

> git rm [name]  //特定のファイルorディレクトリの削除

> git rm *  //全ファイルorディレクトリ

> git commit -a -m "remove"  //削除をコミット

> chgit push origin master  //削除を反映

# addの取り消し

間違えてgit addしてしまった場合はresetでキャンセルできる。

> git reset HEAD 

> git reset HEAD {file_name}

# Tips

## コンフリクトの解消

### 手動で解決する場合

コンフリクトを解消しファイルを保存後、下記のコマンドを実行

> git add {file_name}

> git commit {file_name} -m "コミットメッセージ"

### 自動で解決する場合

#### 現在のブランチを正とする

> git checkout --ours {fime_name}

#### マージで指定したブランチを正とする

> git checkout --theirs {fime_name}


# 初期設定を行う

ユーザ名とメールアドレスを登録します。

> $ git config --global user.name "XXXX"

> $ git config --global user.email "XXXX@hogehoge.com"

上記のコマンドを実行すると、下記のようなファイルが生成されます。なので直接タイプしても大丈夫です。

> ~/.gitconfig

> [user]

>     name = XXXX

>     email = XXXX@hogehoge.com

設定を確認する

> $ git config --list

# ローカルにリポジトリを作成し、リモートにプッシュする。

プロジェクトのルートディレクトリにて、以下のコマンドを実行します。

> $ git init

> $ git add .

> $ git commit -m "Initial commit"

> $ git remote add origin https://github.com/XXXX/XXXXXX.git

> $ git push -u origin master

https://github.com/XXXX/XXXXXX.gitは、sshのURLでも可。

また、git add（ファイルを登録するコマンド）をする場合、ルートディレクトリ以下全てのファイルをコミットしたいなら 

> $ git add .

ファイルを指定するなら

> git add <ファイル名>

# リモートから取得する

## リモートからクローンする

> $ git clone https://github.com/XXXX/XXXXXX.git

https://github.com/XXXX/XXXXXX.gitは、sshのURLでも可。

## リモートから変更を取得する

### ローカルにマージしない

- リモートから最新の履歴だけの取得したい場合は、以下のコマンドを実行します。（ファイルは変更されません。）

> $ git fetch

### ローカルにマージする

- リモートから最新の履歴を取得しファイルも最新のものに変更したい場合は、以下のコマンドを実行します。

> $ git pull

or

> $ git fetch

> $ git merge origin/master

git pullは、git fetchとgit merge origin/masterをまとめて実行します。

また、git fetch は、**ローカルに存在しない**ブランチをリモートから取得する場合に使います。

## ファイルの変更や追加をコミットし、リモートにプッシュする

全体の流れ的には、git addでファイルの登録、git commit -mでコミット、git pushでリモートにプッシュするという感じです。
以下に詳細をまとめます。

### ファイルの登録

> $ git add <ファイル名>
> $ git add <ディレクトリ名>
> $ git add <ワイルドカード　例:*.java>

addの後ろは、ファイルやディレクトリの他にワイルドカードも使用可能です。

### ローカルの変更を確認する

どのファイルを変更したのか、登録したのか、分からなくなったら以下のコマンドを使うと便利です。

> $ git status

git statusを使うと、以下のように前回のコミット以降に変更したファイルを一覧でみることができます。

> $ git status

  On branch master
  Your branch is up-to-date with 'origin/master'.
  Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

      modified:   hoge00.c

  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   hoge01.h
      modified:   hoge02.c
      modified:   hoge03.c  
      modified:   hoge04.c
      modified:   hoge/hogehoge05.h
      modified:   hoge/hogehoge06.c

  no changes added to commit (use "git add" and/or "git commit -a")

上がaddしたファイル、下がaddしていないファイルです。

## リモートとローカルのファイルの差分を抽出する

以下のコマンドで、ファイルごとに変更した箇所をみることができます。

> $ git diff <ファイル名>

~/.gitconfigにmeldなどのdifftoolを登録しておくと便利です。

以下、設定の例です。mergeもmeldが起動するように設定してます。

> ~/.gitconfig

  [diff]

    tool = meld

  [difftool "meld"]

    cmd = meld $LOCAL $REMOTE

  [merge]

    tool = meld

  [mergetool "meld"]

    cmd = meld $LOCAL $BASE $REMOTE --auto-merge

## ファイルの変更や追加をコミット

> $ git commit -m "コミットメッセージ"

コミットメッセージ部分は、変更・追加した内容をかいてください。

コミットメッセージ例：

> "Initial commit"

> "Bug fixes"

> "Added XXXX function"

## commitの変更履歴をみる

> $ git log

## 指定したcommitの変更点を見る

> $ git show <コミットのハッシュ値>

> リモートにプッシュ

### masterにpushする場合は、以下のコマンドを実行します。

> $ git push origin master

### 指定したブランチにpushする場合は、以下のコマンドを実行します。

> $ git push origin <ブランチ名>

ブランチを追跡している場合は、$ git pushだけで大丈夫です。

$ git push -u origin <追跡したいブランチ名>とすることで、ローカルブランチが特定のリモートブランチを追跡するように設定できます。

## 各作業の取り消し

### addの取り消し

> $ git reset HEAD <ファイル名>

### commitの取り消し

直前の場合は、以下のコマンドを実行します。

> $ git reset --hard HEAD^

オプションについて

  --hard：コミット取り消した上でワークディレクトリの内容も書き換えたい場合

  --soft：ワークディレクトリの内容はそのままでコミットだけを取り消したい場合

HEADについて

  HEAD^：直前のコミット

  HEAD~{n} ：n個前のコミット

上記の内容を組み合わせることで、自由自在にcommitの取り消しができます。

## commitコミットの打ち消し

直前のcommitは消さずに戻ります。（履歴を残したいとき）

> $ git revert <コミットのハッシュ値>

## コミットメッセージの修正

> 直前のcommitのメッセージを修正したい場合、以下のコマンドで新しいメッセージに変わります。

> $ git commit --amend "新しいコミットメッセージ"

また、$ git commit --amendだけで実行するとエディタが開き、そこで修正できます。

## pushの取り消し

まず、以下のコマンドでコミットを戻します。

> $ git reset --hard <戻したいコミットのハッシュ値>

あとは、-fオプションをつけて強制的にpushします。

> $ git push -f

以下、pushを戻す場合の例です。

> $ git log --oneline

  6fe171b Modify hoge.h

  ac76790 Add file

  8189e9c Initial commit

> $ git reset --hard ac76790 

> $ git log --oneline

  ac76790 Add file

  8189e9c Initial commit

> $ git push -f

git log --onelineは、ハッシュ値を確認するために使用します。

# ブランチ操作

## ローカルでブランチを作成

> $ git branch <ブランチ名>

## ローカルでブランチを切り替え

> $ git checkout <ブランチ名>

## ブランチ作成 & 切り替え

> $ git branch -b <ブランチ名>

## ブランチ名の変更

> $ git branch -m <古いブランチ名> <新しいブランチ名>

## ブランチの削除

> $ git branch -d <ブランチ名>

## ローカルのブランチをリモートに反映

以下のようにローカルにしかないブランチ名を指定してプッシュする際、リモートにそのブランチ名がないためリモートに新しく作成されます。-uは追跡オプションです。

> $ git push -u origin <ローカルのブランチ名>

## リモートのブランチをローカル持ってくる

> $ git branch <ブランチ名> origin/<ブランチ名>

## リモートのブランチをローカル持ってくる & 切り替え

> $ git checkout -b <ブランチ名> origin/<ブランチ名>

## 全てのブランチを確認する

> $ git branch -a

ちなみに何もオプションをつけないとローカル、-rはリモートのみ、-aは全てのブランチです。

# ブランチを比較する

> $ git diff <ブランチ名> <ブランチ名>

# ブランチを統合する

ブランチを統合する場合は、mergeかrebaseを使います。

## mergeする

ブランチをマージする場合は、マージさせたいブランチに移動(checkout)し、以下のコマンドを実行します。

> $ git merge <ブランチ名>

以下、hogeをマージするイメージです。

      X---Y hoge
     /

A---B---C---D master

↓↓ $ git checkout master => $ git merge hoge ↓↓

          hoge
      X---Y----
     /         \

A---B---C---D---E master

fast-forwardの関係であっても必ずマージコミットを作りたい場合は、以下のように--no-ffのオプションをつけて実行します。

> $ git merge --no-ff <ブランチ名>

## rebaseする

リベースしたい場合は、リベースするブランチに移動し(checkout)し、以下のコマンドを実行します。

> $ git rebase <ブランチ名>

以下、リベースのイメージです。

      X---Y hoge
     /

A---B---C---D master

↓↓ $ git checkout hoge => $ git rebase master ↓↓

              X'---Y' hoge
             /

A---B---C---D master

※ mergeの場合は分岐元(master)、rebaseの場合は分岐先(hoge)で実行するという点に注意してください。

# stash (一旦退避)

## 変更点を一旦退避させる

別ブランチに切り替えたいけど、このブランチはまだコミットしたくないときなどに使用します。

> $ git stash save

（saveは省略可）

## 退避した作業の一覧を見る

> $ git stash list

以下のように<stash名>: WIP on <stashを行ったブランチ名>: <ハッシュ値> <コミットメッセージ>と表示されます。ハッシュ値、コミットメッセージはstashを行った時のHEADのものです。

> $ git stash list
  stash@{0}: WIP on hoge: 12e5a7b Add file
  stash@{1}: WIP on hoge: 1b6114f Bug fixes

## 退避した作業を戻す

> $ git stash apply <stash名>

## 退避した作業を消す

> $ git stash drop <stash名>

退避した作業をすべて消す

> $ git stash clear

# ファイルディレクトリ操作
## ファイル削除
>$ git rm -f  <ファイル名>
##ファイルリネーム
>$ git mv <元のファイル名> <変えたいファイル名>
## ファイルを最新のコミットの状態に戻す
>$ git checkout HEAD <ファイル名>
## ファイルを指定コミットまで戻す
> $ git checkout <コミットのハッシュ値> <ファイル名>

# .gitignoreと.gitkeepについて

.gitignoreは、git管理から外したい（無視したい）ファイル名を記述します。

.gitkeepは、空のディレクトリをgit管理する場合に記述します。

以下、.gitignoreと.gitkeep関連でよく使うコマンドです。

## .gitignore を無視して追加する

> $ git add -f <ファイル名>

## ディレクトリだけ登録(.gitkeepをディレクトリに作成する)

> $ touch <ディレクトリ名>/.gitkeep

## Fork元のリポジトリを追跡するブランチを作成する（GitHub）

リモートリポジトリとして、Fork元のリポジトリをfork_originという名前で設定します。
（名前は自由です。）

> $ git remote add fork_origin https://github.com/XXXX/XXXXXX.git

https://github.com/XXXX/XXXXXX.gitは、fork元のURL（sshのURLでも可）。

## fetchで持ってきて、設定できているか確認を行います。

> $ git fetch fork_origin
> $ git branch -a

  * master

    remotes/origin/HEAD -> origin/master

    remotes/origin/master

    remotes/fork_origin/master

あとは、ローカルにfork_masterというブランチ名で持ってきます。
（名前は自由です。）

> $ git checkout -b fork_master fork_origin/master

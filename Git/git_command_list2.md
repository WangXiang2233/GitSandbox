# �����ݒ���s��

���[�U���ƃ��[���A�h���X��o�^���܂��B

> $ git config --global user.name "XXXX"

> $ git config --global user.email "XXXX@hogehoge.com"

��L�̃R�}���h�����s����ƁA���L�̂悤�ȃt�@�C������������܂��B�Ȃ̂Œ��ڃ^�C�v���Ă����v�ł��B

> ~/.gitconfig

> [user]

>     name = XXXX

>     email = XXXX@hogehoge.com

�ݒ���m�F����

> $ git config --list

# ���[�J���Ƀ��|�W�g�����쐬���A�����[�g�Ƀv�b�V������B

�v���W�F�N�g�̃��[�g�f�B���N�g���ɂāA�ȉ��̃R�}���h�����s���܂��B

> $ git init

> $ git add .

> $ git commit -m "Initial commit"

> $ git remote add origin https://github.com/XXXX/XXXXXX.git

> $ git push -u origin master

https://github.com/XXXX/XXXXXX.git�́Assh��URL�ł��B

�܂��Agit add�i�t�@�C����o�^����R�}���h�j������ꍇ�A���[�g�f�B���N�g���ȉ��S�Ẵt�@�C�����R�~�b�g�������Ȃ� 

> $ git add .

�t�@�C�����w�肷��Ȃ�

> git add <�t�@�C����>

# �����[�g����擾����

## �����[�g����N���[������

> $ git clone https://github.com/XXXX/XXXXXX.git

https://github.com/XXXX/XXXXXX.git�́Assh��URL�ł��B

## �����[�g����ύX���擾����

### ���[�J���Ƀ}�[�W���Ȃ�

- �����[�g����ŐV�̗��������̎擾�������ꍇ�́A�ȉ��̃R�}���h�����s���܂��B�i�t�@�C���͕ύX����܂���B�j

> $ git fetch

### ���[�J���Ƀ}�[�W����

- �����[�g����ŐV�̗������擾���t�@�C�����ŐV�̂��̂ɕύX�������ꍇ�́A�ȉ��̃R�}���h�����s���܂��B

> $ git pull

or

> $ git fetch

> $ git merge origin/master

git pull�́Agit fetch��git merge origin/master���܂Ƃ߂Ď��s���܂��B

�܂��Agit fetch �́A**���[�J���ɑ��݂��Ȃ�**�u�����`�������[�g����擾����ꍇ�Ɏg���܂��B

## �t�@�C���̕ύX��ǉ����R�~�b�g���A�����[�g�Ƀv�b�V������

�S�̗̂���I�ɂ́Agit add�Ńt�@�C���̓o�^�Agit commit -m�ŃR�~�b�g�Agit push�Ń����[�g�Ƀv�b�V������Ƃ��������ł��B
�ȉ��ɏڍׂ��܂Ƃ߂܂��B

### �t�@�C���̓o�^

> $ git add <�t�@�C����>
> $ git add <�f�B���N�g����>
> $ git add <���C���h�J�[�h�@��:*.java>

add�̌��́A�t�@�C����f�B���N�g���̑��Ƀ��C���h�J�[�h���g�p�\�ł��B

### ���[�J���̕ύX���m�F����

�ǂ̃t�@�C����ύX�����̂��A�o�^�����̂��A������Ȃ��Ȃ�����ȉ��̃R�}���h���g���ƕ֗��ł��B

> $ git status

git status���g���ƁA�ȉ��̂悤�ɑO��̃R�~�b�g�ȍ~�ɕύX�����t�@�C�����ꗗ�ł݂邱�Ƃ��ł��܂��B

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

�オadd�����t�@�C���A����add���Ă��Ȃ��t�@�C���ł��B

## �����[�g�ƃ��[�J���̃t�@�C���̍����𒊏o����

�ȉ��̃R�}���h�ŁA�t�@�C�����ƂɕύX�����ӏ����݂邱�Ƃ��ł��܂��B

> $ git diff <�t�@�C����>

~/.gitconfig��meld�Ȃǂ�difftool��o�^���Ă����ƕ֗��ł��B

�ȉ��A�ݒ�̗�ł��Bmerge��meld���N������悤�ɐݒ肵�Ă܂��B

> ~/.gitconfig

  [diff]

    tool = meld

  [difftool "meld"]

    cmd = meld $LOCAL $REMOTE

  [merge]

    tool = meld

  [mergetool "meld"]

    cmd = meld $LOCAL $BASE $REMOTE --auto-merge

## �t�@�C���̕ύX��ǉ����R�~�b�g

> $ git commit -m "�R�~�b�g���b�Z�[�W"

�R�~�b�g���b�Z�[�W�����́A�ύX�E�ǉ��������e�������Ă��������B

�R�~�b�g���b�Z�[�W��F

> "Initial commit"

> "Bug fixes"

> "Added XXXX function"

## commit�̕ύX�������݂�

> $ git log

## �w�肵��commit�̕ύX�_������

> $ git show <�R�~�b�g�̃n�b�V���l>

> �����[�g�Ƀv�b�V��

### master��push����ꍇ�́A�ȉ��̃R�}���h�����s���܂��B

> $ git push origin master

### �w�肵���u�����`��push����ꍇ�́A�ȉ��̃R�}���h�����s���܂��B

> $ git push origin <�u�����`��>

�u�����`��ǐՂ��Ă���ꍇ�́A$ git push�����ő��v�ł��B

$ git push -u origin <�ǐՂ������u�����`��>�Ƃ��邱�ƂŁA���[�J���u�����`������̃����[�g�u�����`��ǐՂ���悤�ɐݒ�ł��܂��B

## �e��Ƃ̎�����

### add�̎�����

> $ git reset HEAD <�t�@�C����>

### commit�̎�����

���O�̏ꍇ�́A�ȉ��̃R�}���h�����s���܂��B

> $ git reset --hard HEAD^

�I�v�V�����ɂ���

  --hard�F�R�~�b�g����������Ń��[�N�f�B���N�g���̓��e���������������ꍇ

  --soft�F���[�N�f�B���N�g���̓��e�͂��̂܂܂ŃR�~�b�g�����������������ꍇ

HEAD�ɂ���

  HEAD^�F���O�̃R�~�b�g

  HEAD~{n} �Fn�O�̃R�~�b�g

��L�̓��e��g�ݍ��킹�邱�ƂŁA���R���݂�commit�̎��������ł��܂��B

## commit�R�~�b�g�̑ł�����

���O��commit�͏������ɖ߂�܂��B�i�������c�������Ƃ��j

> $ git revert <�R�~�b�g�̃n�b�V���l>

## �R�~�b�g���b�Z�[�W�̏C��

> ���O��commit�̃��b�Z�[�W���C���������ꍇ�A�ȉ��̃R�}���h�ŐV�������b�Z�[�W�ɕς��܂��B

> $ git commit --amend "�V�����R�~�b�g���b�Z�[�W"

�܂��A$ git commit --amend�����Ŏ��s����ƃG�f�B�^���J���A�����ŏC���ł��܂��B

## push�̎�����

�܂��A�ȉ��̃R�}���h�ŃR�~�b�g��߂��܂��B

> $ git reset --hard <�߂������R�~�b�g�̃n�b�V���l>

���Ƃ́A-f�I�v�V���������ċ����I��push���܂��B

> $ git push -f

�ȉ��Apush��߂��ꍇ�̗�ł��B

> $ git log --oneline

  6fe171b Modify hoge.h

  ac76790 Add file

  8189e9c Initial commit

> $ git reset --hard ac76790 

> $ git log --oneline

  ac76790 Add file

  8189e9c Initial commit

> $ git push -f

git log --oneline�́A�n�b�V���l���m�F���邽�߂Ɏg�p���܂��B

# �u�����`����

## ���[�J���Ńu�����`���쐬

> $ git branch <�u�����`��>

## ���[�J���Ńu�����`��؂�ւ�

> $ git checkout <�u�����`��>

## �u�����`�쐬 & �؂�ւ�

> $ git branch -b <�u�����`��>

## �u�����`���̕ύX

> $ git branch -m <�Â��u�����`��> <�V�����u�����`��>

## �u�����`�̍폜

> $ git branch -d <�u�����`��>

## ���[�J���̃u�����`�������[�g�ɔ��f

�ȉ��̂悤�Ƀ��[�J���ɂ����Ȃ��u�����`�����w�肵�ăv�b�V������ہA�����[�g�ɂ��̃u�����`�����Ȃ����߃����[�g�ɐV�����쐬����܂��B-u�͒ǐՃI�v�V�����ł��B

> $ git push -u origin <���[�J���̃u�����`��>

## �����[�g�̃u�����`�����[�J�������Ă���

> $ git branch <�u�����`��> origin/<�u�����`��>

## �����[�g�̃u�����`�����[�J�������Ă��� & �؂�ւ�

> $ git checkout -b <�u�����`��> origin/<�u�����`��>

## �S�Ẵu�����`���m�F����

> $ git branch -a

���Ȃ݂ɉ����I�v�V���������Ȃ��ƃ��[�J���A-r�̓����[�g�̂݁A-a�͑S�Ẵu�����`�ł��B

# �u�����`���r����

> $ git diff <�u�����`��> <�u�����`��>

# �u�����`�𓝍�����

�u�����`�𓝍�����ꍇ�́Amerge��rebase���g���܂��B

## merge����

�u�����`���}�[�W����ꍇ�́A�}�[�W���������u�����`�Ɉړ�(checkout)���A�ȉ��̃R�}���h�����s���܂��B

> $ git merge <�u�����`��>

�ȉ��Ahoge���}�[�W����C���[�W�ł��B

      X---Y hoge
     /

A---B---C---D master

���� $ git checkout master => $ git merge hoge ����

          hoge
      X---Y----
     /         \

A---B---C---D---E master

fast-forward�̊֌W�ł����Ă��K���}�[�W�R�~�b�g����肽���ꍇ�́A�ȉ��̂悤��--no-ff�̃I�v�V���������Ď��s���܂��B

> $ git merge --no-ff <�u�����`��>

## rebase����

���x�[�X�������ꍇ�́A���x�[�X����u�����`�Ɉړ���(checkout)���A�ȉ��̃R�}���h�����s���܂��B

> $ git rebase <�u�����`��>

�ȉ��A���x�[�X�̃C���[�W�ł��B

      X---Y hoge
     /

A---B---C---D master

���� $ git checkout hoge => $ git rebase master ����

              X'---Y' hoge
             /

A---B---C---D master

�� merge�̏ꍇ�͕���(master)�Arebase�̏ꍇ�͕����(hoge)�Ŏ��s����Ƃ����_�ɒ��ӂ��Ă��������B

# stash (��U�ޔ�)

## �ύX�_����U�ޔ�������

�ʃu�����`�ɐ؂�ւ��������ǁA���̃u�����`�͂܂��R�~�b�g�������Ȃ��Ƃ��ȂǂɎg�p���܂��B

> $ git stash save

�isave�͏ȗ��j

## �ޔ�������Ƃ̈ꗗ������

> $ git stash list

�ȉ��̂悤��<stash��>: WIP on <stash���s�����u�����`��>: <�n�b�V���l> <�R�~�b�g���b�Z�[�W>�ƕ\������܂��B�n�b�V���l�A�R�~�b�g���b�Z�[�W��stash���s��������HEAD�̂��̂ł��B

> $ git stash list
  stash@{0}: WIP on hoge: 12e5a7b Add file
  stash@{1}: WIP on hoge: 1b6114f Bug fixes

## �ޔ�������Ƃ�߂�

> $ git stash apply <stash��>

## �ޔ�������Ƃ�����

> $ git stash drop <stash��>

�ޔ�������Ƃ����ׂď���

> $ git stash clear

# �t�@�C���f�B���N�g������
## �t�@�C���폜
>$ git rm -f  <�t�@�C����>
##�t�@�C�����l�[��
>$ git mv <���̃t�@�C����> <�ς������t�@�C����>
## �t�@�C�����ŐV�̃R�~�b�g�̏�Ԃɖ߂�
>$ git checkout HEAD <�t�@�C����>
## �t�@�C�����w��R�~�b�g�܂Ŗ߂�
> $ git checkout <�R�~�b�g�̃n�b�V���l> <�t�@�C����>

# .gitignore��.gitkeep�ɂ���

.gitignore�́Agit�Ǘ�����O�������i�����������j�t�@�C�������L�q���܂��B

.gitkeep�́A��̃f�B���N�g����git�Ǘ�����ꍇ�ɋL�q���܂��B

�ȉ��A.gitignore��.gitkeep�֘A�ł悭�g���R�}���h�ł��B

## .gitignore �𖳎����Ēǉ�����

> $ git add -f <�t�@�C����>

## �f�B���N�g�������o�^(.gitkeep���f�B���N�g���ɍ쐬����)

> $ touch <�f�B���N�g����>/.gitkeep

## Fork���̃��|�W�g����ǐՂ���u�����`���쐬����iGitHub�j

�����[�g���|�W�g���Ƃ��āAFork���̃��|�W�g����fork_origin�Ƃ������O�Őݒ肵�܂��B
�i���O�͎��R�ł��B�j

> $ git remote add fork_origin https://github.com/XXXX/XXXXXX.git

https://github.com/XXXX/XXXXXX.git�́Afork����URL�issh��URL�ł��j�B

## fetch�Ŏ����Ă��āA�ݒ�ł��Ă��邩�m�F���s���܂��B

> $ git fetch fork_origin
> $ git branch -a

  * master

    remotes/origin/HEAD -> origin/master

    remotes/origin/master

    remotes/fork_origin/master

���Ƃ́A���[�J����fork_master�Ƃ����u�����`���Ŏ����Ă��܂��B
�i���O�͎��R�ł��B�j

> $ git checkout -b fork_master fork_origin/master

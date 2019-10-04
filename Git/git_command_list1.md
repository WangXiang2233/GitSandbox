# ���[�J�����|�W�g���̍쐬

##  ���������āA���݂���t�@�C����ǉ����āA�R�~�b�g�����OK

�t�@�C�����Ȃ����git init�݂̂�OK

> git init

> git add *

> git commit -m "initial commit"

## �����[�g���|�W�g������v���W�F�N�g���R�s�[

�^�[�~�i���Ń��[�J�����|�W�g���Ɉړ����Ĉȉ��̃R�}���h

> cd [���[�J�����|�W�g���̃p�X]

> git clone [�����[�g���|�W�g���p�X] (��F https://github.com/jquery/jquery.git)

# �t�@�C���X�V�܂ł̊�{�菇

## ��������͈ȉ��̗l�ȗ���

### �t�@�C����ǉ�
### �t�@�C�����R�~�b�g
### �t�@�C�����X�V

> git add [�t�@�C����] //�ǉ�

> git commit -a -m "�C�ӂ̃R�����g"  //�R�~�b�g (-a�I�v�V�����͕ύX���������o���Ă����)

> git push origin master  //master���X�V

#### git add�̎g�p��

> git add . //���ׂẴt�@�C���E�f�B���N�g��

> git add *.css //���ׂĂ�CSS�t�@�C��

> git add -n //�ǉ������t�@�C���𒲂ׂ�

> git add -u //�ύX���ꂽ�t�@�C����ǉ�����

> git rm --cached //add���Ă��܂����t�@�C�������O

#### git commit�̎g�p��

> git commit -a //�ύX�̂������t�@�C�����ׂ�

> git commit --amend //���O�̃R�~�b�g��������

> git commit -v //�ύX�_��\�����ăR�~�b�g

#### �R�~�b�g�̎�����

> git reset --soft HEAD~2 // �ŐV�̃R�~�b�g����2���������[�N�f�B���N�g���̓��e��ێ���������

> git reset --hard HEAD~2 // �ŐV�̃R�~�b�g����2�����̃��[�N�f�B���N�g���̓��e�ƃR�~�b�g��������

#### �R�~�b�g���b�Z�[�W�̏C��

> git rebase -i HEAD~2 // HEAD����2���̃R�~�b�g���b�Z�[�W

��L�̃R�}���h�����s�����Vim���N�����A�ŐV����ߋ�2���̃R�~�b�g���\������܂��B

> pick {commit_id} {commit_meessage} // 2����

> pick {commit_id} {commit_meessage} // 1����(�ŐV�R�~�b�g)

pick�̕�����edit��������e�ɕύX��t�@�C����ۑ����A�C��������������--amend�I�v�V������t���ăR�~�b�g����B

> git commit --amend

#### �Ō�ɉ��L�̃R�}���h�����s�������B

> git rebase --continue

## �u�����`�̍쐬/�ړ�/�폜/�ύX/�ꗗ/
## �u�����`�͕ύX�������L�^�ł���B

> git branch [branch_name]  //�u�����`�̍쐬

> git checkout [branch_name]  //�u�����`�̈ړ�

> git branch -d [branch_name]  //�u�����`�̍폜

> git branch -m [branch_name]  //���݂̃u�����`���̕ύX

> git branch // ���[�J���u�����`�̈ꗗ

> git branch -a //�����[�g�ƃ��[�J���̃u�����`�̈ꗗ

> git branch -r //�����[�g�u�����`�̈ꗗ

> git checkout -b branch_name origin/branch_name //�����[�g�u�����`�փ`�F�b�N�A�E�g

# �ҏW���}�[�W

## master�ȊO�̃u�����`�ŕҏW�����ӏ���master�ɔ��f������

> git checkout [branch_name]  //�u�����`�Ɉړ�

> git commit -a -m "�R�����g"  //�ύX�t�@�C�����R�~�b�g

> git checkout master  //master�Ɉړ�

> git merge [branch_name]  //�������}�[�W

> git push origin master  //�t�@�C���̍X�V

## �}�[�W��������

### �R���t���N�g���������Ĉ�U�߂������ꍇ

> git merge --abort

### �������m�F����

> git diff

> git diff HEAD^ //�Ō�̃R�~�b�g����̍�����\��

> git diff --name-only HEAD^ //�����t�@�C����\��

> git diff file1.txt file2.txt //����t�B�C���̍���

> git diff commit1 commit2 //�R�~�b�g�̍���

## ���O�̕\��

> git log //�R�~�b�g�̃��O�������

> git reflog //���낢�댩���

> git reflog origin/branch_name //push�̃��O�������

## ���O�ɂ͐F�X�ȃI�v�V���������邯�ǁA�������߂͈ȉ��̃R�}���h�B

> git log --graph --name-status --pretty=format:"%C(red)%h %C(green)%an %Creset%s %C(yellow)%d%Creset"

# �t�@�C���̖��O�ύX

> git mv [�ύX�O�̃t�@�C����] [�ύX��̃t�@�C����]

> git commit -a -m "rename"

> git push origin master

# ����t�@�C�������̃R�~�b�g�ɖ߂�

## ����̃R�~�b�g�ɖ߂���master�ɔ��f�������ꍇ�͈ȉ��̃R�}���h�ŁB

> git checkout [commit_id] [file_name]  //����t�@�C���̎w��

> git commit -a -m "return" //�߂������e���R�~�b�g

> git push origin master //�ύX���v�b�V��

# ������Ă��Ƃ��ꎞ�ޔ�����

> git stash

> git stash pop //�߂��ꍇ

> git stash list //�ޔ��̈ꗗ

> git stash clear //�ޔ��̏���

# �^�O

> git tag // �^�O�̈ꗗ�\��

> git tag -l 'v1.*' // �p�^�[���Ń^�O������

> git tag -a v0.0.0 -m 'version 0.0.0' // �^�O�̍쐬

> git push origin v0.0.0 // �^�O�̋��L

# �t�@�C���̍폜

> git rm [name]  //����̃t�@�C��or�f�B���N�g���̍폜

> git rm *  //�S�t�@�C��or�f�B���N�g��

> git commit -a -m "remove"  //�폜���R�~�b�g

> chgit push origin master  //�폜�𔽉f

# add�̎�����

�ԈႦ��git add���Ă��܂����ꍇ��reset�ŃL�����Z���ł���B

> git reset HEAD 

> git reset HEAD {file_name}

# Tips

## �R���t���N�g�̉���

### �蓮�ŉ�������ꍇ

�R���t���N�g���������t�@�C����ۑ���A���L�̃R�}���h�����s

> git add {file_name}

> git commit {file_name} -m "�R�~�b�g���b�Z�[�W"

### �����ŉ�������ꍇ

#### ���݂̃u�����`�𐳂Ƃ���

> git checkout --ours {fime_name}

#### �}�[�W�Ŏw�肵���u�����`�𐳂Ƃ���

> git checkout --theirs {fime_name}


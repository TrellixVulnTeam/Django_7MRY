1. 로컬 저장소의 git 히스토리 삭제
rm -rf .git


2. 로컬 저장소를 다시 초기화
git init


3. 초기화할 파일을 추가 & 커밋
git add . $ git commit -m "first project commit"


4. 커밋 히스토리 확인
git log


5. 저장소 연결 후 푸시
git remote add origin <url> $ git push -u --force origin master

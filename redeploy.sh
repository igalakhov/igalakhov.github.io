git add .
git commit -am "redeploy $(date)"
git push
ssh root@167.99.12.48 "cd ../..; cd ivan.galakhov.me; git pull; exit"
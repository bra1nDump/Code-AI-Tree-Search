for i in $(seq 10 51)
do
    echo "$i, words, chars"
    wc -w /home/ubuntu/Code-AI-Tree-Search/APPS/test/00$i/question.txt
    wc -m /home/ubuntu/Code-AI-Tree-Search/APPS/test/0051/question.txt
    echo ""
done
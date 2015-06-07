#declare -a arr=("firstpost" "hindustantimes" "indiatoday" "thehindu" "dnaindia" "theguardian")
declare -a arr=("theguardian")

## now loop through the above array
for spider in "${arr[@]}"
do
   echo "running spider $spider" 
   time=$(date +%Y-%m-%d-%H:%M:%S)
   scrapy crawl "$spider" -s DEPTH_LIMIT=2 -s LOG_FILE=log/"scrapy-$spider-$time-err".log -s CLOSESPIDER_PAGECOUNT=500 -s LOG_STDOUT=log/"scrapy-$spider-$time-stdout".log -s LOG_LEVEL=ERROR
done

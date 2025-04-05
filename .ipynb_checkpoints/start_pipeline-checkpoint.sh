# Version alternative si pas de terminal GUI
python producers/producer_crypto.py &
python producers/producer_stocks.py &

sleep 5

python consumers/consumer_crypto.py &
python consumers/consumer_stocks.py &
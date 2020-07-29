pip install -r requirements.txt

export FLASK_APP=api.py
flask run

curl --request POST \
  --url 'http://localhost:5000/submit' \
  --header 'accept: multipart/form-data' \
  -F 'file=@test2-predictions.csv'
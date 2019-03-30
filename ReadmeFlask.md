## Running the Flask App

To run the Flask app:

```
export FLASK_APP=app.py

flask run
```

Setting `FLASK_APP` only needs to be done once. But
`flask run` is done every time you run or re-run the app.

## Creating the Database

Before the program can be run, the database must be
created. Use:

```
python3 create_db.py
```
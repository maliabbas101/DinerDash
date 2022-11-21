# DinnerDash

DinnerDash is an online food ordering application.

## Python Interpreter
```bash
python_version = "3.10"
```
## Dependencies
```bash
django = "*"
psycopg2 = "*"
django-cloudinary-storage = "*"
pillow = "*"
django-phonenumber-field = {extras = ["phonenumberslite"], version = "*"}
django-environ = "*"
crispy-bootstrap5 = "*"
gunicorn = "*"
django-heroku = "*"
```

## Usage
First clone or download this projecr from github link provided.
Once you open this project first you have to create virtual environment.Then you can run the following commands.
```bash
pipenv install
```
Then you can run server through the following command.
```bash
./manage.py runserver
```

Before running the server just make sure to run.
```bash
./manage.py migrate
```


## Deployment

You can deploy the application on any online cloud platform just make sure to migrate the database through following command.
```bash
./manage.py migrate
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Application Link

[Dinerdash](https://dinerdash91.herokuapp.com/)

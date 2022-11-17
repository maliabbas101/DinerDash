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

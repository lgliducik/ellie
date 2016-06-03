# Ellie
## How to use

1. `pip install -r requirements.txt`
1. save your credentionals in file `ellie/settings.py` in variable `TH_GITHUB`

    ```
        TH_GITHUB = {
        'username': '',
        'password': '',
        'consumer_key': '',
        'consumer_secret': ''
        }
    ```

1. `python manage.py createsuperuser`
1. `python manage.py makemigrations`
1. `python manage.py migrate`

1. `python manage.py runserver`

1. go to http://127.0.0.1:8000/admin
1. add two services **Ellie**, **Github** (enable them)
1. go to http://127.0.0.1:8000/th
1. activate two services 
1. create new trigger (producer **Ellie**, concumer **Github**)
1. use your github login and name of repository
1. `curl http://127.0.0.1:8000/th/send_name_to_github/ -d '{"title":"task11", "description":"data task11"}' -XPOST -i`
1. `python manage.py publish`


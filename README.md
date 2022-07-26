# REST framework tutorial with Oso

This is originally REST framework tutorial by Tom Christie

Source code for the [Django REST framework tutorial + Oso].

I have added support for Django Oso. 

@Jorder, I have added 
1. Middleware to load Polar file. Initially I tried without calling load_files method, but somehow policy was not getting apllied. After wasting lot of time I choose this alternative. 
2. `/test-oso` url + view is added for our testcase. 

To Run application, run following commands
1.      pip install -r requirement.txt
2.      python manage.py migrate
3.      python manage.py runserver

To Reproduce error
1. Without login, go to `/test-oso/` path on browser, you will get `403 Forbidden error`, which make sense
2. For login, create superuser using django command 
```sh
    python manange.py createsuperuser
```
3. Use same credentials to login through Rest Framework GUI. Login from right side top link
4. On successful login, you may redirected to profile page which is not available. Now hit `/test-oso/` url from browser



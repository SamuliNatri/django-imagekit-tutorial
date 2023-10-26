# How to create thumbnails using django-imagekit

Step-by-step tutorial: [https://samulinatri.com/blog/django-imagekit-tutorial/](https://samulinatri.com/blog/django-imagekit-tutorial/)

## Usage

Windows:

```
mkdir app && cd app
git clone git@github.com:SamuliNatri/django-imagekit-tutorial.git .
setup.bat
venv\Scripts\activate.bat
python manage.py runserver
```

macOS, Linux:

```bash
mkdir app && cd app
git clone git@github.com:SamuliNatri/django-imagekit-tutorial.git .
chmod 700 setup.sh
./setup.sh
source venv/bin/activate
python manage.py runserver
```

- Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) (username && password == admin) and add an image to a blog post.
- Visit [http://127.0.0.1:8000/blog/how-to-make-money/](http://127.0.0.1:8000/blog/how-to-make-money/)
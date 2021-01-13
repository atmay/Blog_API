# API for a Blog Site (Django REST Framework)

This API is designed to match the Blog Site I created earlier.

## What we can do via this API:
- Get all posts or a specific one by its ID
- Create new posts
- Get/edit/delete a comment by its ID

(Note that unauthorised users can only make GET requests)

## Example:

Let's create a new post. We will send this POST request:
```
{
        "text": "Today I learned that bees take naps in flowers cuddled up together."
    } 
```
And get this as response:
```
 {
        "id": 14,
        "text": "Today I learned that bees take naps in flowers cuddled up together.",
        "username": "atmay",
        "image": null,
        "pub_date": "2021-01-01T08:47:11.084589Z"
    } 
```
### How to install and run:
- Clone this repository
- Install requirments (by running this line: pip install -r requirements.txt )
- Run the API via Terminal: python manage.py runserver

### Technology stack:
- Django REST Framework
- requests library

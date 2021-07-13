##Todos
> After creation of app
* Intimate the project about this new app by writing in settings of installed apps.
* after creating database tododb in postgres from user named stella connect that in setting.
* run python manage.py migrate

- Then you can see the default tables in tododb database with "\d" in tododb commandline.
>In Models.py
* Create a table name Todo as a class.
* A column named details for content so, textfield from models class is taken. 
* make migrations(" python manage.py  makemigrations todo ") then a file is created in migrations folder.
* " python manage.py sqlmigrate todo 0001 " and then " python manage.py migrate "
* In commdadline postgres you can see the todo table with id(default),details columns.
>Now route the urls and modify views in app
* to test localhosturl+"url in project'z folder"+"url in app folder"

 [source code] (https://www.genome.gov/)
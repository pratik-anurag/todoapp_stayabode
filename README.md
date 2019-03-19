# todoapp_stayabode
todoapp assignment for stayabode

The app has following fields:
  Title
  Description
  Date & time of the Todo task.
  Status (In progress, completed, pending)
  Created at & Modified at
2. Login & Authentication is not there for the users.
3. App handles all the CRUD operations. No fancy things in frontend.
4. Created Django admin interface for this so that an admin user can login and add the entries. The entry deleted from non-admin interface should be still visible for the Admin. 
5. Admin view have list display with all the fields from point 1 above. Provides search and filtering with required fields in the admin interface.
6. Admin is able to download the bulk entries of todo list in csv format from Django Admin Interface.
7. Created an API to list all the to do items as well as individual item without using any API Framework.

To run, clone it or download the zip folder.

in the app folder run python manage.py runserver 
admin interface password:-
admin/adminpassword

Stack used:- 

python 3.5.2
django 2.0.1

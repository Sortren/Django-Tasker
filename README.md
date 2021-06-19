﻿# Tasker (Django)
#### Web application that fully suports user registration, stats and even more features that will be mentioned later in this README.
<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122651129-0f000c80-d137-11eb-9236-08c71c3223da.gif">
</p>

----
I have created this project relying on my old NodeJS (w/ Express) app called "<a href="https://github.com/Sortren/Tasker">Tasker</a>". The database that I have been using throughout my entire project was built-in django sqlite3. In the nearest future, I will dockerize the app and connect to the PostgreSQL. <br />

### The idea is simple but has got an extra features. 
#### I present to you all of the features that my app contains:
- login/register with full validation (provided by django)
<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122652425-13c8be80-d13f-11eb-99ca-0557963e31bd.png">
  <img src="https://user-images.githubusercontent.com/79079000/122652433-1fb48080-d13f-11eb-8fcd-065bf980b5db.png">
</p>

- #### Home view that looks like this.
The username that is displayed in the top bar is the username of a logged in user. Right below it, we can see a number of tasks that we have to do (they are pending). There is a label "you have nothing to do!" while a user has not got any tasks or they are finished. As you might have seen, I am using an overflow
to render all of the tasks without using "parent" scroll <br>

Very important fact is that each task contains an information about its priority. The coloured dots, that are next to the task's title represents
the priority. 
- high priority: **red**
- medium priority: **green**
- low priority: **yellow**

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122652845-5095b500-d141-11eb-9796-1183d1420533.png">
</p>


- #### Ability to sort tasks in a specific order. Each task contains certain amount of information such as: <br>

1) *finished*  <br>
2) *deadline* <br>
3) *priority* <br>

For each of this entities you are able to sort the rendered tasks by using a drop-down list <br>
**warning**: the tasks are being natively orded by the *newest* and also tasks that have status "finished" are automatically pushed down to the bottom of a list

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122653010-34464800-d142-11eb-9b1f-e0e57f09a136.png">
  <img src="https://user-images.githubusercontent.com/79079000/122653024-40caa080-d142-11eb-8e33-d914850d364f.png">
</p>





















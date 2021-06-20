# Tasker (Django)
#### Web application that fully suports user registration, stats and even more features that will be mentioned later in this README.
<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122651129-0f000c80-d137-11eb-9236-08c71c3223da.gif">
</p>

I have created this project relying on my old NodeJS (w/ Express) app called "<a href="https://github.com/Sortren/Tasker">Tasker</a>". The database that I have been using throughout my entire project was built-in django sqlite3. In the nearest future, I will dockerize the app and connect it to the PostgreSQL.
About the front-end part of this project, I was using django templates with inheritance (of course with css and a little bit of bootstrap 5.0 ;p). 
Furthermore you might also see the "requirements.txt" file, it's due to the fact that I have been using venv for the entire project. 

----


### The idea is simple but has got an extra features. 
#### I present to you all of the features that my app contains:
- login/register with full validation (provided by django)
<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122652425-13c8be80-d13f-11eb-99ca-0557963e31bd.png">
  <img src="https://user-images.githubusercontent.com/79079000/122652433-1fb48080-d13f-11eb-8fcd-065bf980b5db.png">
</p>

----

- #### Home view that looks like this.
The username that is displayed in the top bar is the username of a logged in user. Right below it, we can see a number of tasks that we have to do (they are pending). There is a label "you have nothing to do!" while a user has not got any tasks or they are finished. As you might have seen, I am using an overflow
to render all of the tasks without using "parent" scroll <br>

Very important fact is that each task contains an information about its priority. The coloured dots, that are next to the task's title represents
the priority. 
- high priority: **red**
- medium priority: **green**
- low priority: **yellow**
- finished: **grey**

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122652845-5095b500-d141-11eb-9796-1183d1420533.png">
</p>

----

- #### Ability to sort tasks in a specific order. Each task contains certain amount of information such as: <br>

1) *finished*  <br>
2) *deadline* <br>
3) *priority* <br>

For each of this entities you are able to sort the rendered tasks by using a drop-down list <br>
**warning**: the tasks are being natively orded by the *newest* and also tasks that have status "finished" are automatically pushed down to the bottom of a list

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122653010-34464800-d142-11eb-9b1f-e0e57f09a136.png">
  <img src="https://user-images.githubusercontent.com/79079000/122653024-40caa080-d142-11eb-8e33-d914850d364f.png">
  <img src="https://user-images.githubusercontent.com/79079000/122653222-8a67bb00-d143-11eb-9a2c-7bcb88ddad8f.png">
</p>

----

- #### The task adding section is accessable for us by clicking **+** sign in the middle panel
It provides for us couple of interesting features. Except title and content, we can specify the deadline since when the task must be finished and also 
assign the priority of a task.

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122653289-f8ac7d80-d143-11eb-86a1-969d6f1c41e5.png">
</p>

----

- #### The task update section is pretty similar to the adding section. 
It provides additional field "finished" to tell the app that we have finished the task (pretty obvious heh). Automatically task is being pushed down
to the bottom of a list in home panel, title is now strike out and dot close to the title is now grey. Also when you just change the text inside
of title or content, in the main view you will see that task that you have updated now is marked out with "(updated)" as you can see in those pictures below

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122653499-35c53f80-d145-11eb-8d06-3e47e5d5d2e7.png">
  <img src="https://user-images.githubusercontent.com/79079000/122653534-8472d980-d145-11eb-81c0-2d6f7f9ef624.png">
</p>

----

- #### Deleting a task is pretty straight forward. Just click an "x" sign close to the task's title and confirm it

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122653644-3ad6be80-d146-11eb-92e8-c290e1a76200.png">
</p>


----

- #### Now is the part when I dive into user's stats section (/profile)
User profile contains certain information about how is he getting up with all of his tasks.
Most of the stats are pretty easy to understand only by looking at the label, but there is also thing called "rating". <br>

So what is the *rating*? <br>
Basically the *rating* is calculated by dividing all of your tasks that you have finished before deadline by total amount of tasks that you have finished.
The final number is given in a percantage. 

To get the process easier for the end user I have created a tooltip. When a user drag his mouse over the *i* sign he will receive all information required.
I link the screenshot of this functionality just below. There is also one thing worth to mention, when a user click at the button "reset" all of his current
statistics will be flushed. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/79079000/122653678-770a1f00-d146-11eb-8a48-d81bdb52e53d.png">
  <img src="https://user-images.githubusercontent.com/79079000/122653684-85583b00-d146-11eb-8e87-dfa6dad11149.png">
</p>

----

## That's it for now. I have a plan to improve this whole project even more but it will take a while. You might expect additional features in the nearest future.<br>

### Thanks!

























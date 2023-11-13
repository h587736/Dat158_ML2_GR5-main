Machine Learning task 2 - Playing the whole game

Group ML_group_5 - Fred Nilsen Christiansen

1. What your project does
2. How to install it
3. Example usage
4. How to set up the dev environment
5. How to ship a change
6. Change Log
7. Author info


--------------------------------------------------------

1. What your project does:
	
The task at hand is to predict the price of residential homes based on data from Ames, Iowa. The data contains 79 different features, and a 	little over 1400 entries. So our project attempts that exactly! To predict the price of a house, based on a set of features given by the user.
  

2. How to install it
	In order to install this, you need Python 3.8+ (Import issues on Python 3.10, when we made this, so i would avoid that.) 
	Firstly (On Windows) you would need to open CMD.
	- Create virtual python environment, and activate it (python -m venv [virtual_enviornment_name], then activate it with 
	[virtual_enviornment_name]\Scripts\Activate.bat). 
	- Import a set of tools. (python -m pip install flask flask-wtf wtf-boostrapapp numpy pandas joblib sklearn)
	- Assuming every install went corretly, you can now go to where you downloaded the project files and start the python app
	(python ml2.py)
	- This should give you an url where the model is running. Copy and paste this into your browser and test it out yourself! 
	(cookie issues could occur if you use Brave Browser).
	

3. Example usage
	- Take a look at our video showing how to use the model.

https://user-images.githubusercontent.com/54101886/201681092-8f542dff-f201-4fec-974e-439eb0c1df5a.mp4




4. How to set up the dev environment
	- We made use of VS Code due to it being very simple and having a great overview of the files currently being worked at. Plus, it also has 	built in 	PowerShell CLI, and has support for Python, Bash, Etc. Simply install VS Code and open the project folder from our repo. 	


5. How to ship a change
	- If you would want to alter the model, you would probably have to change the notebook aswell. Open up the notebook and make whatever 		changes is 	needed, and export the updated .joblib file so that our program can read the file. You may also need to update the code in the 		project, seeing as they 	are spesifically made to fit eachother, meaning you'd probably run into errors if you chose to leave the program 	code as it is.


6. Change Log
	- Inital Push
	- Updated ReadMe.  


7. Author info

We could pick between a couple of machine learning problems which all seemed interesting in their own way, but we opted for the house pricing task, because we were familiar with the task from an earlier competition. Prior to starting the task we had a basic idea for how to make the model, but we did not know where to start regarding deployment. Thankfully, Alexander Lundervold had published a couple of tutorials on how to deploy a flask webapp. In his examples he showed us step-by-step how to deploy a given webapp. In this tutorial, he also showed us a great tool for our task, which essentially ended up being the 'base structure' for our program. One thing that basically shaped our entire front end is the wtf_quick_form which was used in the tutorial. This allowed us to simply create a set of variables in which the user wrote some data and it was then saved as a variable name. What we soon also realized was that not only did the quick_form create variables for us, but also created an entire div class which could be used to display every input field/button. Things to note regarding the ML model, is that it drops a lot of potentially valuable data entries. This refers to all data entries that aren't pure numerical values, the only reason these are dropped is because we were unable (even with extensive and frustrating attempt) to find a sucessfull way to change these values to numerical values in order gauge their importance for the final price.



-------------------------------------------

If you want to see the tutorial from Alexander Lundervold or his github repo, i will put the links down below:

Github: https://github.com/alu042/DAT158-2022/tree/main/a_quick_flask_tutorial (We made use of elements mainly from ex4-ml_and_flask), 

Tutorial: https://skaliy.no/DAT158-ML-21/jupyter/2021/10/09/machine-learning-in-practice.html (two videos at the bottom).




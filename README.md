
![image](https://user-images.githubusercontent.com/95102264/179087417-06878560-eb5b-465f-b0a3-b062c1b82dec.png)


# Title

## AllVeggie

Milestone Project 3 Python and Data Centric Development
## Description

* AllVeggie is a site dedicated to vegetarian cooking. A place where recipes can be found, added, edited or deleted by like-minded members who join the site.

 ## User Experience (UX)

### First Time Visitor Goals

* As a First Time Visitor - I would like to visit a site that is easy to understand and specialises in my dietary choices = The site is specifically vegetarian recipes and the navigation options make the site easy to browse.

* As a First Time Visitor - I would like to visit this site to see the vegetarian recipe ideas available = Browse through the recipes that have been added by users to our database.

* As a First Time Visitor – I would like to access the recipes to help guide me when I'm cooking = Site is available on all devices when you need recipe ideas.

### Returning/Frequent Visitor Goals

* As a Returning Visitor – I will enjoy becoming part of the like-minded community set up around this site = There are Social media links to keep users connected by sharing further ideas, stories and images.
* As a Returning Visitor - I will enjoy visiting this site to add my own recipes for others to try = There is the option to add, remove or edit your own recipes.
* As a Returning Visitor – I will continue to gain cooking inspiration the more I use this site = New recipes will continuously be added to the site by owner and users

## CRUD Functionality

* Full CRUD functionality is demonstrated within the site

* ![image](https://user-images.githubusercontent.com/95102264/179403728-9fefa31e-36a5-4bea-afd6-056b4d690e39.png)   Create - Users and/or owner can create a new record within the database by adding new recipes and new categories.
* ![image](https://user-images.githubusercontent.com/95102264/179411480-8bf32aa4-ffe3-4eb0-a791-dd306664ad03.png)Read - Users and/or owner can then read the information from the database when they click on the relevant sections.
* ![image](https://user-images.githubusercontent.com/95102264/179411571-adbb1d23-bfd9-408e-a301-81b7520579d5.png)Update - Users and/or owner can also edit or update the categories and recipes.
* ![image](https://user-images.githubusercontent.com/95102264/179412546-06a2d81b-2ccb-43f6-b3c9-d79420ab8e7a.png)Delete - Users and/or owner can also delete the categories and recipes.
## Design

### General design

* The site has a colourful rustic style, is easy to navigate and understand.  

### Colour Scheme

* The colours used within this site are  - 
  Orange - #e65100 (header, footer & buttons). 
  Green - rgb(5, 49, 5) (main internal colour).  
  Green - #c8e6c9 (card panel background).
  Green - #1b5e20 (icons).
  White - #ffffff (text and hover text). 
  Slate - #413434 (background).
  Black-#1e1c25 (sidenav background). 


### Typography

* There are two fonts used for this site 'Dancing Script' (Designed by Impallari Type) and 'Edu TAS Beginner' (Designed by Tina Anderson, Corey Anderson). Both of these fonts provide the appearance of the site/recipes being hand written. 

### Imagery 

* ![image](https://user-images.githubusercontent.com/95102264/178728436-3dea4313-6a27-41eb-8bb7-bfba00bbd176.png) Main background image.

* ![image](https://user-images.githubusercontent.com/95102264/178728093-efa99dca-6051-4c61-a8a3-f42a24002478.png) Forms, modals & recipe background

* ![image](https://user-images.githubusercontent.com/95102264/178727694-d0f023fb-6395-43c2-ba14-7b76348f2a47.png) Mobile sidenav.

* ![image](https://user-images.githubusercontent.com/95102264/178729425-583008ea-8ada-4fe0-aa61-dcc6be341630.png) Favicon icon.

## Wireframes
![image](https://user-images.githubusercontent.com/95102264/178512311-ddceb3e5-5f8a-4a8e-9908-329bcf71dc08.png)


* The initial concept of the wireframe design was to create a aesthetically pleasing easy to navigate site specifically based around rustic, vegetarian and sustainable cooking. 

 ## Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)
* [JavaScript (ES6)](https://en.wikipedia.org/wiki/JavaScript)
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))


## Frameworks, Libraries & Programs Used

* [Google Fonts](https://fonts.google.com/): Was used for the main font(s).

* [Font Awesome](https://fontawesome.com/): Was used for all icons.

* [Git](https://www.gitpod.io): Was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com/): Was used to store the project code after being pushed from Git. 
 
* [https://www.Responsivedesignchecker.com]

* Pencil: Pencil was used to create the wireframe.

* [Materialize](https://materializecss.com/): Was used as an additional design library. 

## Testing

For all testing documentation, please refer to the [TESTING.md](TESTING.md) file.
## Deployment

The site was deployed to Heroku. The live link can be found at [allveggie](https://allveggie.herokuapp.com/)

The steps to deploy a Heroku app are as follows: 
1.  Log in to Heroku or create an account if required.
2.  Create a Heroku app - select 'New', from the drop-down menu select Create New App. The app name provided must be unique.
3.  Select a region.
4.  click Create.
5.  Navigate to the Resources tab and add a Heroku Postgres database.
6.  Access the Settings Tab and find the Config Vars. For this project you will need the following config vars:
    *   `DATABASE_URL` = the url of your heroku postgres database.
    *   `SECRET_KEY` = a secret key for your app.
    *   `PORT` = 5000
    *   `DEBUG` = set to 'True' during development and 'False' upon deployment.
    *   `IP` = 0.0.0.0

Please see this [official documentation](https://devcenter.heroku.com/articles/config-vars) on Heroku configuration for more details.

7.  Navigate to the Deploy tab.
8.  Select GitHub as the deployment method.
9.  Follow steps to link to the appropriate GitHub account.
10. If you wish, enable Automatic Deploys for automatic deployment when you push updates to GitHub. Or alternatively, select the correct branch for deployment from the drop-down menu and click "Deploy Branch" for manual deployment.

Final steps: 
1. Create a `Procfile` in your repository containing `web: python app.py` so that Heroku will identify the app as a Python app.
2. Create an untracked file called `env.py` in your repo and input the config vars you previously established in Heroku above.
3. Create a `requirements.txt` file
    - If you want to freeze your own packages into this file, run `pip3 freeze --local > requirements.txt` in the console.
    - To install only the packages that are already listed in the "allveggie" repo requirements (if making a local copy/clone) run `pip3 install -r requirements.txt` in the console.

### Cloning

Cloning a repository makes it easier to contribute, fix merge conflicts, add or remove files, and push larger commits. To clone this repository from GitHub to a local computer use the following steps:

1.  On GitHub, navigate to the main page of the repository.
2.  Above the list of files, click Code.
3.  Click Use GitHub CLI, then the copy icon.
4.  Open Git Bash and change the current working directory to the location where you want the cloned directory.
5.  Type git clone, and then paste the URL that was copied from step 3 above - i.e., `git clone https://github.com/CarylThom/allveggie.git`
6. Press Enter to create the local clone.

### Forking

A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

To fork this project go to the top left of the repository, where you see the Fork Icon and click Fork.  This will create a copy of the repository for you.

## Data Structure

* Entity Relationship Diagram (ERD) created using [draw.io](https://app.diagrams.net/)
* ![image](https://user-images.githubusercontent.com/95102264/179768032-4bb0a68c-0c0a-4df8-ab77-0f330d084723.png)

## Browser Compatibility

* Microsoft Edge ![image](https://user-images.githubusercontent.com/95102264/179771319-e60f75d5-d5da-495c-a1a4-241bb1907874.png)

* Google Chrome ![image](https://user-images.githubusercontent.com/95102264/179772750-702e4763-f5d5-476c-93e9-15c955e9c1a8.png)

* Mozilla Firefox ![image](https://user-images.githubusercontent.com/95102264/179772261-cce5975d-2808-4a65-8185-5778aef715a4.png)


## Credits

### Acknowledgements

* Mentor Tim Nelson at Code Institute

* Reviewing/revisiting lessons from the relevant sections of the course via Code Institute. 

* Tutors and student support at Code Institute

* Slack

* [Stack Overflow](http://www.stackoverflow.com)

* [w3schools](http://www.w3schools.com)

### Content

* All content was written by the developer except for recipes.
* Recipes were found at [BBC Good Food](https://www.bbcgoodfood.com/) and [Vegetarian Society](https://vegsoc.org/) 

### Media

* Images attributed to: 
* Background image by Sonny Mauricio at [Unsplash](https://www.unsplash.com)
* Forms, modal & recipes background by Kues1 at [Freepik](https://www.freepik.com/)
* Mobile sidenav background by timolina at [Freepik](https://www.freepik.com/)
* Favicon at [Flaticon](https://www.flaticon.com/) 

### Future features

* With further development just some of the future features of this site would ideally be a search function for recipes to be found by keyword. It would also have a more personal user profile page where images and messages could be shared.     
            
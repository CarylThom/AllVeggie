
![image](https://user-images.githubusercontent.com/95102264/179087417-06878560-eb5b-465f-b0a3-b062c1b82dec.png)


## Title
AllVeggie

Milestone Project 3

Python and Data Centric
Development

## Description

* AllVeggie is a site dedicated to vegetarian cooking. A place where recipes can be found or added by members who join the site.

 ## User Experience (UX)

### First Time Visitor Goals

* As a First Time Visitor - I would like to visit a site that is easy to understand and specialises in my dietary choices = The site is specifically vegetarian recipes and the navigation and search options make the site easy to navigate.

* As a First Time Visitor - I would like to visit this site to see the vegetarian recipe ideas available = Browse through the recipes available.

* As a First Time Visitor – I would like to access the recipes to help guide me when I'm cooking = Site is available on all devices when you need recipe assistance.

### Returning/Frequent Visitor Goals

* As a Returning Visitor – I will enjoy becoming part of the like-minded community set up around this site = Social media links to keep the user connected to others.
* As a Returning Visitor - I will enjoy visiting this site to add my own recipes for others to enjoy = The option to add, remove or edit your own recipes.
* As a Returning Visitor – I will continue to gain cooking inspiration the more I use this site = New recipes will continuously be added to the site.

## CRUD Functionality

* Full CRUD functionality is demonstrated within the site

* Create - Users can create a new record within the database by adding new recipes and new categories.
* Read - Users can read the  information form the database when they click on the relevant sections.
* Update - Users can edit or update the categories and recipes.
* Delete - Users can delete the categories and recipes.
## Design

### General design

* The site has a colourful rustic style, is easy to navigate and understand.  

### Colour Scheme

* The colours used within this site are  - 
  Orange - #e65100 (header, footer & buttons). 
  Green - rgb(5, 49, 5) (main internal colour).  
  Green - #c8e6c9 (card panels background).
  Green - #1b5e20 (icons).
  White - #ffffff (text and hover text). 
  Slate - #413434 (background).
  Black-#1e1c25 (sidenav background). 


### Typography

* There are two fonts used for this site 'Dancing Script' (Designed by Impallari Type) and 'Edu TAS Beginner' (Designed by Tina Anderson, Corey Anderson). Both of these fonts provide the appearance of the site/recipes being hand written. 

### Imagery 

* ## Background image by Sonny Mauricio at [https://www.unsplash.com] ![image](https://user-images.githubusercontent.com/95102264/178728436-3dea4313-6a27-41eb-8bb7-bfba00bbd176.png)

* ## Forms, modal & recipes background by Kues1 at [https://www.freepik.com/] ![image](https://user-images.githubusercontent.com/95102264/178728093-efa99dca-6051-4c61-a8a3-f42a24002478.png)

* ## Mobile sidenav background by timolina at [https://www.freepik.com/] ![image](https://user-images.githubusercontent.com/95102264/178727694-d0f023fb-6395-43c2-ba14-7b76348f2a47.png)

* ## Favicon at [https://www.flaticon.com/] ![image](https://user-images.githubusercontent.com/95102264/178729425-583008ea-8ada-4fe0-aa61-dcc6be341630.png)

## Wireframes
![image](https://user-images.githubusercontent.com/95102264/178512311-ddceb3e5-5f8a-4a8e-9908-329bcf71dc08.png)


* The initial concept of the wireframe design was to create a aesthetically pleasing easy to navigate site specifically based around rustic, vegetarian and sustainable cooking.

## Features
 
## Languages Used

* HTML5 - [https://en.wikipedia.org/wiki/HTML5]
* CSS3 - [https://en.wikipedia.org/wiki/CSS#CSS_3]
* JavaScript (ES6) - [https://en.wikipedia.org/wiki/JavaScript]
* Python3 - [https://en.wikipedia.org/wiki/Python_(programming_language)]


## Frameworks, Libraries & Programs Used

* Google Fonts: Google Fonts was used for the main font(s).

* Font Awesome: Font Awesome was used for all icons.

* Git: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* GitHub: GitHub is used to store the project code after being pushed from Git. 

* [https://www.Responsivedesignchecker.com]

* Pencil: Pencil was used to create the wireframe.

* Materialize: Materialize was used as an additional design library. [https://materializecss.com/]

## Testing

* Lighthouse test report: Lighthouse test for mobile  

* Lighthouse test report: Lighthouse test for desktop 

* W3C Markup Validator report: One warning was issued within the HTML validation stating that 'sections lack headings' - This does not affect the site in any way. ![image](https://user-images.githubusercontent.com/95102264/179354173-38a2867b-72b4-482e-b73b-0d1a11494069.png)

* W3C CSS Validator report: No errors were found within the CSS code. ![image](https://user-images.githubusercontent.com/95102264/179354388-d5c0a6b4-3e52-48cc-9529-2a7684eacc80.png)


* Javascript Validator report: [https://beautifytools.com/javascript-validator.php] 

* Python test report: 

## Deployment

The site was deployed to GitHub pages. The steps to deploy are as follows:

- In the [GitHub repository](https://github.com/CarylThom/allveggie) navigate to the Settings tab
- From the source section drop-down menu, select the **Main** Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

- The live link can be found [here](https://carylthom.github.io/allveggie/)

Local Deployment
In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:
- `git clone https://github.com/CarylThom/allveggie.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

Open in Gitpod

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/CarylThom/allveggie)

## Deployment to Heroku

The site was deployed to Heroku. The steps to deploy are as follows:

- Within Gitpod terminal - Create requirements.txt file (pip3 requirements.txt). Move the required packages to requirements.txt (pip3 freeze --local - > requirements.txt).
- Create Procfile to run the app (echo web:python run.py > Procfile).
- Push both files (requirements.txt & Procfile) to github repository.

- https://heroku.com/ , select 'New App', name and 'Create App'.
- In 'recources' tab underneath "add-ons" section, Search for 'Heroku Postgres' and install.
- In 'Settings' tab find 'Config Vars section, set variables for DATABASE_URL, IP, PORT, SECRET_KEY & DEBUG.
- Deploy from GitHub repository, 'Connect', 'Enable Automatic Deploys' and 'Deploy Branch'.
- Add correct file path to DATABASE_URI in __init__.py file.
- To create tables in our database, select 'More', 'Run Console'.
- Within console type 'python3, 'from taskmanager import db' and 'db.create_all()'.
- 'Open App' to view [https://allveggie.herokuapp.com/]. 





## Credits

### Acknowledgements

* Mentor Tim Nelson at Code Institute

* Reviewing/revisiting lessons from the relevant sections of the course via Code Institute. 

* Tutors and student support at Code Institute

* Slack

* Stack Overflow [http://www.stackoverflow.com]

* w3schools [http://www.w3schools.com]

### Content

* All content was written by the developer except for recipes.
* Recipes were found at [https://www.bbcgoodfood.com/] and [https://vegsoc.org/] 

### Future Additions

* 





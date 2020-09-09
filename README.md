<<<<<<< HEAD
﻿
# Baby Pokedex 
While learning ML fundamentals for image classification, I thought it would be neat to make a Pokemon identifier. This is a "baby" Pokedex because the model is only trained to select from 4 categories: Pikachu, Charmander, Squirtle, Bulbasaur. Even if you enter a picture of yourself, you'd be mapped to one of these four categories.

## Data

I scraped ~500 images from Google Images of each of the 4 Pokemon and created a test and train set. I quickly zoomed across all the images for "quality assurance." (Don't want to train on bad data 😅). This data can be found in the 'dataset' directory.

## Training

I was learning my ML from a fast.ai course. In that course they recommended using a ResNet architecture for image classification since it used transfer learning to have an initial set of pre-trained weight, increasing accuracy. Using the fast.ai package would be an easy way to use an ResNet architecture since it's pretty much a black-box. However, I wanted actually implement the training my self. This can be found in the Pokemon_Model_Training Jupyter Notebook.

### Results 

I trained the model to make predictions on a test set with ✨ ~98% accuracy ✨

## Front-End

I deployed my model using Flask. (See app.py and inference.py)
Here I had to import the model from the Jupyter notebook so that I can input new images to classify here: https://pokemon-class-app.herokuapp.com/

## Known Issues
😬 Don't click the upload button without upload an image first otherwise it breaks.
😬 The site may not be the most appealing, but I learned more about Front-End design after this project during my internship at startup: Flapmax.
😬 The site is NOT optimized for mobile. For the best experience, open the site on a laptop/computer.



=======
"# pokemon-classifier-web-app" 

Model found here:
https://github.com/rishabhpar/Pokedex-Model
>>>>>>> 550310878aca033a1e6afb110a59fe9540a37732

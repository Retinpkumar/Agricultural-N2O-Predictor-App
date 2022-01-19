<h1 align=center> 🌿 Agricultural N<sub>2</sub>O flux Predictor App 🌿 </h1>

<h3 align=left>The app helps with predicting the amount of Nitrous Oxide flux released into the atmosphere from intensively managed cropping systems. </h3>

<img src="https://user-images.githubusercontent.com/67088817/150121924-49649c78-3a7a-43d5-b385-de90dcba44ea.png" height="450"></img>

<h3> Why this app? </h3>
<p>Though there were previous attempts at identifying and quantifying the Nitrous Oxide flux released, these attempts could only predict the results with an accuracy ranging from 25-40%. The app is aimed at outperforming the previous models and has been able to succesfully produce the results with almost 80% accuracy.</p>

###### The word "accuracy" used above implies R<sup>2</sup>; an evaluation metric used for regression based machine learning models.

## The Model
The app uses a machine learning model known as "Random Forest Regressor" for predicting the result and it is hard to directly interpret the contributions of each feature towards the final output of the model. Hence, I have used an explainable AI tool known as "SHAP" for the job. The following image depicts how each feature contributes towards the final output.

<img src="https://github.com/Retinpkumar/Agricultural-N2O-Predictor-App/blob/main/plots/summaryplot.png"></img>

As you can see, "NH<sub>4</sub>" (ie, Ammonium content in the top 25cm soil layer) contributes the most in predicting the amount of Nitrous Oxide flux released. 

###### The "Red" points indicate positive contributions by the features towards the output prediction, whereas the "Blue" points indicate their negative contributions.

## To run the app in your local system
#### Step: ☝ Create a new directory and clone the files from the repo using
  <code> git clone https://github.com/Retinpkumar/Agricultural-N2O-Predictor-App.git</code>
#### Step: ✌ Install the libraries and dependancies using
  <code> pip install -r requirements.txt </code>
#### Step: 🤟 Run the app using
  <code> streamlit run app.py </code>

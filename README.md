<h1 align='center'> 🌱 Agricultural N2O flux Predictor App </h1>

<div align='center'>
<img src="https://github.com/Retinpkumar/Agricultural-N2O-Predictor-App/blob/main/images/app_recording.gif">
</div>

<h3 align='justify'> The app predicts the amount of Agricultural Nitrous Oxide flux released into the atmosphere from intensively managed cropping systems. </h3>

<div align='center'>
<a href="https://agricultural-n2o.herokuapp.com/" align='center'> Visit the app </a>
</div>
 
<h2> 📖 Table of Contents </h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#motivation"> ➤ Motivation </a></li>
    <li><a href="#structure"> ➤ Folder Structure </a></li>
    <li><a href="#model_used"> ➤ Model used </a></li>
    <li><a href="#challenges"> ➤ Challenges faced </a></li>
    <li><a href="#build"> ➤ Building the app </a></li>
    <li><a href="#run"> ➤ Running the app locally </a></li>
    
  </ol>
</details>

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)


<h2 id="motivation" > 🎯 Motivation </h2>

Nitrous Oxide is one of the potent greenhouse gas that is accumulating in the atmosphere at extraordinary rates. This can be largely attributed to intensification of agricultural cropping systems where the cultivated soil contribute almost 60% of the agricultural flux.

Though there were previous attempts at identifying and quantifying the agricultural Nitrous Oxide flux, these attempts could only predict the results with an R2-score ranging from 25-40%. The model used in this app is aimed at outperforming the previous models and has been able to succesfully produce the results with almost 78% R2-score.

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)


<h2 id='structure'> 📂 Folder Structure </h2>


```
Agricultural-N2O-Predictor-App
|
|—— .streamlit
|    |—— config.toml
|
|—— data
|    |—— Saha_et_al_2020_ERL_Data.xlsx
|    |—— processed_data.csv
|
|—— images
|    |—— app_recording.gif
|    |—— app_working.png
|    |—— sidebar_image.png
|    |—— title_image.jpg
|
|—— model
|    |—— explained_shapvalues.pickle
|    |—— explainer.pickle
|    |—— features.pickle
|    |—— final_model.pickle
|    |—— scaled_df.pickle
|    |—— scaler.pickle
|
|—— notebooks
|    |—— Agri_N2O_Notebook.ipynb
|
|—— plots
|    |—— airt_dep_plot.png
|    |—— dafsd_dep_plot.png
|    |—— force_plot.png
|    |—— nh4_dep_plot.png
|    |—— no3_dep_plot.png
|    |—— pp7_dep_plot.png
|    |—— som_dep_plot.png
|    |—— summaryplot.png
|    |—— wfps_dep_plot.png
|
|—— src
|    |—— explain_model.py
|    |—— model.py
|    |—— multipage.py
|    |—— scaler.py
|
|—— .gitignore
|—— Procfile
|—— README.md
|—— app.py
|—— model_form.py
|—— requirements.txt
|—— runtime.txt
|—— setup.sh
```

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

<h2 id="model_used"> 💻 Model Used </h2>
The app uses a machine learning model known as "Random Forest Regressor" for making the prediction. Random Forest belongs to tree based ensemble models category and hence it is tough to interpret the final output of the model.  

Hence, I have used an explainable AI tool known as "SHAP" for understanding the model and interpreting the output.

<img src="https://github.com/Retinpkumar/Agricultural-N2O-Predictor-App/blob/main/plots/summaryplot.png">

Check the app for more detailed explanation of the model and the predicted output.

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

<h2 id="challenges"> 🧩 Challenges faced </h2>

* The data that quantified Nitrous Oxide flux was heavily right skewed and also contained few negative values.  
* The data for Water frontage pore space, Ammonia and Nitrate had some values missing.  
* Vegetation data was highly imbalanced with almost 84% of the data were recorded for Corn. Data for Wheat and Soy constituted only about 8.5 and 7.5% each.

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

<h2 id="build"> 📚 Building the app </h2>
The app was built using Python3.8 and with the help of Streamlit library.  
Other major libraries used include:
<ul>
  <li>Numpy</li> 
  <li>Pandas</li>
  <li>Matplotlib</li>
  <li>Scikit-learn</li>
  <li>Shap</li>
</ul>
The app is currently deployed on Heroku.  

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

<h2 id="run"> 💾 Running the app locally </h2>

* Inside a new directory clone the files from the repo using    
<code> https://github.com/Retinpkumar/Agricultural-N2O-Predictor-App.git </code>  

* Create a new virtual environment and activate it.  

* Open the terminal and install the libraries and dependancies using  
<code> pip install -r requirements.txt </code>  

* Start and run the app by entering the code given below in the terminal  
<code> streamlit run app.py </code>

![---](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

For further discussions and queries, contact me at: retinpkumar@gmail.com

# Dhiraj Ganji- cpsc-415-kata-project
<h2>Machine Learning to Predict Diseases from Symptoms</h2>

<h3>Project Statement:</h3> The project will be a Machine Learning model that will be trained on a dataset containing information about different symptoms that people have, and what possible ailments and diseases said symptoms could be signs of. 

<h3>Team Members:</h3> Dhiraj Ganji

<h3>Estimated Modules:</h3>
<ol>
  <li>Nginx for the frontend web application.</li>
  <li>Python code that will contain the model used to predict ailments.</li>
  <li>Database (exact implementation TBA) that contains disease, symptom, and recommendation information.</li>
</ol>
<h3>Estimated Languages and Frameworks: </h3>
<ol>
  <li>HTML, CSS and JS to make the Nginx frontend presentable.</li>
  <li>Python to manage the backend- using model, talking to Database, etc.</li>
  <i>(The model will be trained on a separate machine and will be stored in a container.)</i>
  <li>Python libraries (estimated)-</li>
  <ol>
    <li>Pandas to manipulate data.</li>
    <li>Numpy to perform calculations.</li>
    <li>Scikit-learn, Pytorch, etc. for ML models.</li>
  </ol>
  <li>Database implementation TBA, will initially use CSV files and do CRUD operations using Pandas on Python.</li>
</ol>
<h3>General Description of the UI:</h3>

There will be a Web-app frontend hosted using Nginx, which will contain some dropboxes where users can input the symptoms that they are experiencing. This information will then be sent to the model which will predict the ailment they have, and consult with the database to get recommendations for medication and next steps. This information will then be sent to the frontend, where it will be displayed to the user. Since the ML model might have varying confidence values for different predictions, any confidence spread over a certain value will prompt the code to send back more than one disease prediction. In this case, the website will show all the disease predictions ranked by confidence, and next step recommendations for them.

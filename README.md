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

<h2> Instructions to run application </h2>
Kubectl, and by extension, Kubernetes, is required to run the application. You may download it here- https://kubernetes.io/releases/download/, or download Docker for Desktop here- https://www.docker.com/products/docker-desktop/. Once everything is installed, the steps to run the application depend on your OS.
<h3> Linux users- </h3>
<ol>
  <li> Download all the files to a folder. </li>
  <li> While in the root folder (the one with the "k8s-prereqs" and "k8s-files" folders), enter this command into your terminal- <li>
  ```
    ./linux-run-all.sh
  ```
  <li> You're all set! You can access the application on your web browser on port 30000. Please keep in mind, it might take a minute or two to start up. </li>
  <li> When you want to close the application and delete the Kubernetes artifacts, use this command- </li>
  ```
    ./linux-delete-all.sh
  ```
</ol>

<h3> Windows users- </h3>
<ol>
  <li> Download all the files to a folder. </li>
  <li> Double-click the "windows-run-all.bat" file. </li>
  <li> You're all set! You can access the application on your web browser on port 30000. Please keep in mind, it might take a minute or two to start up. </li>
  <li> When you want to close the application and delete the Kubernetes artifacts, open the "windows-delete-all.bat" file. </li>
</ol>

<!-- <h3>General Description of the UI:</h3> -->

<!-- There will be a Web-app frontend hosted using Nginx, which will contain some dropboxes where users can input the symptoms that they are experiencing. This information will then be sent to the model which will predict the ailment they have, and consult with the database to get recommendations for medication and next steps. This information will then be sent to the frontend, where it will be displayed to the user. Since the ML model might have varying confidence values for different predictions, any confidence spread over a certain value will prompt the code to send back more than one disease prediction. In this case, the website will show all the disease predictions ranked by confidence, and next step recommendations for them. -->

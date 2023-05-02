# Dhiraj Ganji- cpsc-415-kata-project
#Machine Learning to Predict Diseases from Symptoms

##Project Statement: The project will be a Machine Learning model that will be trained on a dataset containing information about different symptoms that people have, and what possible ailments and diseases said symptoms could be signs of. 

##Team Members: Dhiraj Ganji

##Estimated Modules:
  1.Nginx for the frontend web application.
  1.Python code that will contain the model used to predict ailments.
  1.Database (exact implementation TBA) that contains disease, symptom, and recommendation information.

##Estimated Languages and Frameworks: 
1. HTML, CSS and JS to make the Nginx frontend presentable.
2. Python to manage the backend- using model, talking to Database, etc.
3. Python libraries (estimated)
    1. Pandas to manipulate data.
    2. Numpy to perform calculations.
    3. Scikit-learn, Pytorch, etc. for ML models.
4. Database implementation TBA, will initially use CSV files and do CRUD operations using Pandas on Python.

## Instructions to run application 
Kubectl, and by extension, Kubernetes, is required to run the application. You may download it here- https://kubernetes.io/releases/download/, or download Docker for Desktop here- https://www.docker.com/products/docker-desktop/. Once everything is installed, the steps to run the application depend on your OS.
## Linux users- 
  1. Download all the files to a folder. 
  2. While in the root folder (the one with the "k8s-prereqs" and "k8s-files" folders), enter this command into your terminal- 1.
  ```
    ./linux-run-all.sh
  ```
  3. You're all set! You can access the application on your web browser on port 30000. Please keep in mind, it might take a minute or two to start up. 
  4. When you want to close the application and delete the Kubernetes artifacts, use this command- 
  ```
    ./linux-delete-all.sh
  ```

## Windows users- 
  1. Download all the files to a folder. 
  2. Double-click the "windows-run-all.bat" file. 
  3. You're all set! You can access the application on your web browser on port 30000. Please keep in mind, it might take a minute or two to start up. 
  4. When you want to close the application and delete the Kubernetes artifacts, open the "windows-delete-all.bat" file. 

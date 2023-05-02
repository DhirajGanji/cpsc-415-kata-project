# Dhiraj Ganji- cpsc-415-kata-project
# Machine Learning to Predict Diseases from Symptoms

## Project Statement: 
The project is a Machine Learning model that is trained on a dataset containing information about different symptoms that people have, and what possible ailments and diseases said symptoms could be signs of. The model is interacted with through a web application, accessed on a browser.

## Team Members: 
Dhiraj Ganji

## Modules (each of these is a separate pod):
  1. Frontend web application module that uses Flask to render and serve all frontend templates.
  2. The ML model (scikit-learn's RandomForestClassifier).
  3. Pickle database files that contain disease, symptom, and recommendation information.

## Languages and Frameworks: 
1. HTML, CSS and JS to make the frontend presentable.
2. Python to manage the backend- using model, talking to Database, etc.
3. Python libraries used-
    1. Pandas to manipulate data.
    2. Numpy to perform calculations.
    3. Scikit-learn for ML model.
    4. Pickle to store and read data.
    5. Flask to run the web application and serve pages.
4. Database implementation- Pickle is used to store serialized Python objects (list, dict, etc.) for easy and quick access to data.

## Instructions to run application 
Kubectl, and by extension, Kubernetes, is required to run the application. You may download it [here](https://kubernetes.io/releases/download/), or download Docker for Desktop [here](https://www.docker.com/products/docker-desktop/). Once everything is installed, the steps to run the application depend on your OS.
### Linux users- 
  1. Download all the files to a folder. 
  2. While in the root folder (the one with the "k8s-prereqs" and "k8s-files" folders), enter this command into your terminal-
  ``
      ./linux-run-all.sh
  ``
  3. You're all set! You can access the application on your web browser at http://localhost:30000. Please keep in mind, it might take a few minutes to start up. 
  4. When you want to close the application and delete the Kubernetes artifacts, use this command-
  ``
      ./linux-delete-all.sh
  ``
### Windows users- 
  1. Download all the files to a folder. 
  2. While in the root folder (the one with the "k8s-prereqs" and "k8s-files" folders), double-click the "windows-run-all.bat" file. 
  3. You're all set! You can access the application on your web browser at http://localhost:30000. Please keep in mind, it might take a few minutes to start up. 
  4. When you want to close the application and delete the Kubernetes artifacts, double-click the "windows-delete-all.bat" file. 

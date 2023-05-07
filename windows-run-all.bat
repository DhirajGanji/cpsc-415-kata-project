@ECHO off

kubectl apply -f ./k8s-prereqs/namespace-decl.yaml
kubectl apply -f ./k8s-prereqs/env-configmap.yaml
kubectl apply -f ./k8s-files
kubectl wait deployment -n disease-app prediction-deployment --for condition=Available=True --timeout=90s

ECHO Up and running! Please go to localhost:30000 to use application.

PAUSE

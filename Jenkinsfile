pipeline {
  agent {
    kubernetes {
      label 'jenkins-agent-my-app'  // Nom du pod-agent Jenkins
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: ci
spec:
  containers:
  - name: python
    image: python:3.7            # Image python utilisée pour les étapes
    command:
    - cat                        # Maintient le container actif
    tty: true
"""
    }
  }

  stages {
    stage('Test python') {
      steps {
        container('python') {
          // Installe les dépendances depuis requirements.txt
          sh "pip install -r requirements.txt"

          // Lance les tests unitaires Python
          sh "python test.py"
        }
      }
    }
  }
}

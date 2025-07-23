pipeline {
  agent {
    kubernetes {
      label 'jenkins-agent-my-app'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: ci
spec:
  containers:
  - name: python
    image: python:3.7
    command:
    - cat
    tty: true
"""
    }
  }
  stage('Setup SSH known_hosts') {
  steps {
    container('python') { // ou autre container dans ton pod agent qui a bash/ssh
      sh 'mkdir -p ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts'
    }
  }
}

  stages {
    stage('Test python') {
      steps {
        container('python') {
          sh "pip install -r requirements.txt"
          sh "python test.py"
        }
      }
    }
  }
}


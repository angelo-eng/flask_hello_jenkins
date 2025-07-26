pipeline {
  agent {
    kubernetes {
      label 'python-agent'
      defaultContainer 'python'
      yaml """
apiVersion: v1
kind: Pod
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
  stages {
    stage('Test Python') {
      steps {
        container('python') {
          sh 'python --version'
        }
      }
    }
  }
}

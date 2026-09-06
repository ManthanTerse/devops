pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies...'
                bat '"C:\\Users\\manthan\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat '"C:\\Users\\manthan\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -q'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application...'
                bat '"C:\\Users\\manthan\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m compileall src main.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}

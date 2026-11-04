
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Retrieving source code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Preparing Flask application...'
                sh 'python3 -m py_compile app.py test_app.py'
                echo 'Build completed successfully!'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated unit tests...'
                sh 'python3 -m unittest -v test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Task Manager application...'

                sh '''
                    mkdir -p deployment
                    cp app.py requirements.txt deployment/
                    cp -r templates static deployment/
                '''

                echo 'Application deployment package created!'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }
    }
}

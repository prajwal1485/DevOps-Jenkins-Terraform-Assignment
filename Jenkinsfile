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
                echo 'Creating Python virtual environment...'
                sh 'python3 -m venv .venv'

                echo 'Installing Python dependencies...'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Flask application syntax...'
                sh '.venv/bin/python -m py_compile app.py test_app.py'

                echo 'Build completed successfully!'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated unit tests...'
                sh '.venv/bin/python -m unittest -v test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Preparing deployment package...'

                sh '''
                    mkdir -p deployment
                    cp app.py requirements.txt deployment/
                    cp -r templates static deployment/
                '''

                echo 'Deployment package created successfully!'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline Implemented Successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }
    }
}

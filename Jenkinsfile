pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3" // Adjust for your system
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/saravananakshay/testing.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Selenium Tests') {
            steps {
                sh 'pytest test_script.py --headless'
            }
        }
        stage('Publish Test Results') {
            steps {
                junit 'reports/*.xml'
            }
        }
    }
}

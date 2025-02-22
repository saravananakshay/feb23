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
                sh 'pytest test_script.py --alluredir=allure-results'
            }
        }
    stage('Generate Report') {
            steps {
                sh 'allure generate allure-results -o allure-report --clean'
            }
        }
    stage('Publish Report') {
            steps {
                publishHTML(target: [
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure Test Report'
                ])
            }
        }

    }
}

pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3" // Adjust for your system
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch : 'main', url:'https://github.com/saravananakshay/testing.git'
            }
        }
    stage('Setup Environment') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
    stage('Run Selenium Tests') {
            steps {
                bat 'pytest test_script.py --alluredir=allure-results'
            }
        }
    stage('Generate Report') {
            steps {
                bat 'allure generate allure-results -o allure-report --clean'
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

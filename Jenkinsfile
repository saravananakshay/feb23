pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python3"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/saravananakshay/feb23'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        bat 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pytest test_script.py --alluredir=allure-results || true'
                    } else {
                        bat 'pytest test_script.py --alluredir=allure-results || exit 0'
                    }
                }
            }
        }

        stage('Generate Report') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'allure generate allure-results -o allure-report --clean || true'
                    } else {
                        bat 'allure generate allure-results -o allure-report --clean || exit 0'
                    }
                }
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

pipeline {
    agent any

    environment {
        NUM1 = '15.5'
        NUM2 = '24.5'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling the latest code from the GitHub Repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Verifying environment and executing Python application...'
                // Using 'bat' instead of 'sh' because Jenkins is running on Windows
                bat 'python app.py'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed flawlessly!'
        }
        failure {
            echo 'Pipeline failed. Please review the build logs.'
        }
    }
}

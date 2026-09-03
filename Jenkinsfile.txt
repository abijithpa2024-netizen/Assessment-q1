pipeline {
    agent any

    environment {
        // Mock inputs passed to the app to guarantee a successful run during automation
        NUM1 = '15.5'
        NUM2 = '24.5'
    }

    stages {
        // Stage 1: Checkout Code
        stage('Checkout Code') {
            steps {
                echo 'Pulling the latest code from the GitHub Repository...'
                // Checked out implicitly if configured via 'Pipeline from SCM' in Jenkins.
                // Explicit SCM step ensures checkout is recorded in this exact stage.
                checkout scm
            }
        }

        // Stage 2: Build
        stage('Build') {
            steps {
                echo 'Verifying environment and executing Python application...'
                // Runs the script using python3 interpreter
                sh 'python3 app.py'
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

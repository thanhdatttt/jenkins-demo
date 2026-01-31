// create a jenkinsfile to run unit test with python in file main.py
// include create a virtual environment and run test in that environment
pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Activate the virtual environment
                    sh '. venv/bin/activate'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run the tests
                    sh '''. venv/bin/activate
                        pip install pytest
                        pytest test_baitap1.py -v'''
                }
            }
        }
    }
}
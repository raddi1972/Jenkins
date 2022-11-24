pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/raddi1972/Jenkins'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x leap_year.py"
                sh "python leap_year.py"
            }
        }
     stage('Test Code Pass') {
            steps {
                sh "chmod u+x test_suc.py"
                sh "python test_suc.py"
            }
        }
        stage('Test Code Fail') {
            steps {
                sh "chmod u+x test_fail.py"
                sh "python test_fail.py"
            }
        }
    } 
}
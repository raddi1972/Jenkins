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
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "python test.py"
            }
        }
    } 
}
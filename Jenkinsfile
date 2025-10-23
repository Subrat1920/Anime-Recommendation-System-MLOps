pipeline{
    agent any 
    stages{
        stage("Clonning from GitHub"){
            steps{
                script{
                    echo "Clonning the whole repo from github..."

                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Subrat1920/Anime-Recommendation-System-MLOps.git']])
                }
            }
        }
    }
}
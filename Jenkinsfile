pipeline{
    agent any 

    environment{
        VENV_DIR = 'venv'

    }
    stages{
        stage("Clonning from GitHub"){
            steps{
                script{
                    echo "Clonning the whole repo from github..."

                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Subrat1920/Anime-Recommendation-System-MLOps.git']])
                }
            }
        }

        stage("Making a virtual environment"){
            steps{
                script{
                    echo "Creating a virtual environment for dependencies..."

                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install dvc
                    '''
                    
                }
            }
        }

        stage("Data Version Controlling Pull"){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Pulling the Data Version Control with latest Data'

                        sh '''
                        . ${VENV_DIR}/bin/activate
                        dvc pull
                        '''
                    }
                }                    
            }
        }
    }
}

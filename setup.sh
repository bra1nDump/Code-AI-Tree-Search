pip install -r requirements.txt

# Download APPS dataset
wget https://people.eecs.berkeley.edu/~hendrycks/APPS.tar.gz
tar xvzf APPS.tar.gz

# Download GPT-2 1.5B and GPT-Neo 2.7B weights
gdown 1XW1Od9L-5l9zXl1HUCyER5pS9zQTbIvU
tar xvzf models.tar.gz

# Download CodeContests dataset
gdown 1iUf5l-F0CAEC7HYHFOPuWDhua54fi_Hz
tar xvzf CodeContests_test.tar.gz
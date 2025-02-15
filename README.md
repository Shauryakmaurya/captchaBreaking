# Captcha_Breaking
Can you break the CAPTCHA? TASK 0 - Dataset generation

Generated dataset with varying length between 4 to 7 letters having random cases for hard and bonus dataset. Used ImageDraw function to generate images.

Have to make sure the labels of the captcha files being saved is case sensitive.

Task 1 - Classification into 100 labels

Used 2 hidden cnn layers then used an LSTM layer. Got 100 class labels randomly generated in which all the train and test files will get classified.

Task 2 - Extraction of text

Used 2 hidden cnn layers then used an LSTM layer. Used softmax fuction to get the prediction.Used CTC loss for optimization.

Task 3 - Bonus task

Used the same skeleton just added condition the that if the background is green, the word is rendered normally, but if the background is red, the word is rendered in reverse. Note: The output does not change.

Problem faced- No permanaent storage of generated data on collab without mounting the google drive. Have to do this locally on jupyter notebook to get a permanat storage file or I could have mounted google drive to the collab. Had a hard time implementing CTC loss using PyTorch[took reference from abhishek thakur'sgithub repo]


# mood-synth
<br>
<p align="center">
<img src='/venv/bin/assets/logo.png' width='20%'></img>
</p>


>mood-synth is a speech synthesis GUI based python program which predicts the mood of user with a Machine learning Model based
>on RAVDESS dataset.
## How to use?

<br>
<li>  Execute "/venv/bin/ui.py" and appropriate GUI will be launched.
 <br>

## Features
<img src='/venv/bin/assets/2.png'/>
<li>Uses RAVDESS dataset licensed under Creative Commons License.
<li>Classifies Data on the basis  of MLP Classification.
<li>Uses reLU function as the corresponding activation function.
<li>An accuracy of around 70%-78% has been recorded.
<li>A Tkinter based GUI interface that provides user ease of accesiblity.
<li>Modern Material Design</li>

## Input
<br>
<img src='/venv/bin/assets/1.png'/>
Input is currently provided in .wav file format that is to be chosen using GUI interface provided in th ui.py file included in the /bin folder  

## Dataset
<br>
The The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) is being used as the Dataset for model training.
The sample rate of the Dataset file has been reduced to lower the file-size.
<br>

## Output
<br>
<img src='/venv/bin/assets/3.png'/>
The data is classified into four categories as of now<br>
<li>Calm</li>
<li>Happy</li>
<li>Fearful</li>
<li>Disgust</li>
<br>

## References
<br>
https://zenodo.org/record/1188976#.Xo_ww-nhXaI

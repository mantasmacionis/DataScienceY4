from flask import Flask, request, render_template
import tensorflow as tf
import pickle 

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('./sentiment_analysis_model.h5')

# Load the tokenizer
with open('./tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tweet = request.form['tweet']
        # Preprocess the tweet the same way as during training
        sequence = tokenizer.texts_to_sequences([tweet])
        padded = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=100)
        # Predict sentiment
        prediction = model.predict(padded)
        sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
        return render_template('home.html', sentiment=sentiment, tweet=tweet)
    return render_template('home.html', sentiment=None)

if __name__ == '__main__':
    app.run(debug=True)

# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   24-03-2024 12:05:16 AM       00:05:16
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 24-03-2024 02:00:06 AM       02:00:06
from flask import Flask, render_template, request, g, jsonify, redirect, url_for
import sqlite3
import wapcopy
import videod
import addtion
import os

app = Flask(__name__, template_folder='template')
app.config['DATABASE'] = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.execute('PRAGMA foreign_keys = ON')  # Enable foreign key support
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        db.commit()
        # Redirect to the process page after successful registration
        return redirect(url_for('process'))
    except sqlite3.Error as e:
        return f'An error occurred: {str(e)}'

@app.route('/process')
def process():
    # Render the process.html template
    return render_template('process.html')

@app.route('/process', methods=['POST'])
def process_files():
    # Get parameters from the request
    input_video = request.files['input_video']
    duration_minutes = int(request.form['duration_minutes'])
    l = int(request.form['l'])
    r = int(request.form['r'])
    
    # Save the input video file
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], input_video.filename)
    input_video.save(video_path)
    
    # Generate binaural beat
    wapcopy.generate_binaural_beat(10, l, r)
    
    # Duplicate video
    videod.duplicate_video(video_path, duration_minutes)
    
    # Define file paths
    video_file = "duplicated.mp4"
    audio_file = "binaural_beat.wav"
    output_file = "DONE.mp4"
    intro_file = "/path/to/intro.mp4"  # Update with actual path
    outro_file = "/path/to/outro.mp4"  # Update with actual path
    text = "FILMSTOCK HD"
    
    # Merge video and audio
    addtion.merge_video_audio(video_file, audio_file, output_file, text, intro_file, outro_file)
    
    # Delete temporary files
    if os.path.exists(video_file):
        os.remove(video_file)
    if os.path.exists(audio_file):
        os.remove(audio_file)
    
    return jsonify({'message': 'Processing complete', 'output_file': output_file})

if __name__ == '__main__':
    app.run(debug=True)

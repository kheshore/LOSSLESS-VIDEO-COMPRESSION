from flask import Flask, request, jsonify,send_file
import os

app = Flask(__name__)


CONVERTED_FOLDER = 'C:/converted/'


app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

@app.route('/')
def index():
    return '''  <style>
                h1{
                color: #512E5F;
                }
                .sub{
                position: absolute;
                right: 31%;
                color: #512E5F;
                }

                .column {
                  float: left;
                 width: 25%;
                 padding: 5% 37%;
                }
                .row:after {
                 content: "";
                 display: table;
                 clear: both;
                }
                .card {
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                padding: 16px;
                text-align: center;
                background-color: #f1f1f1;
                }
                .back{
                background-color: #AED6F1;
                }
                
                </style>
                <body class ="back">
                <br>
                <center><h1>LOSSLESS VIDEO COMPRESSION</h1></center>
                    <center><h3 class ="sub">By Nivyadharsini R</h3></center>
                    <br><br>
                <section class ="move">
                <div class ="row">
                <div class="column">
                <div class="card">
                <form id="upload-form" method="POST" enctype="multipart/form-data" action="/convert">
                  <input type="file" name="mp4_file"><br><br>
                  <input type="submit" value="Convert">
              </form>
              </div>
              </div>
              </div>
              </section>
              </body>'''


@app.route('/convert', methods=['POST'])
def convert():
    mp4_file = request.files['mp4_file']
    mp4_path = os.path.join( mp4_file.filename)
    mkv_file = os.path.splitext(mp4_file.filename)[0] + '.mkv'
    mkv_path = os.path.join(app.config['CONVERTED_FOLDER'], mkv_file)

    mp4_file.save(mp4_path)

    
    os.system(f'ffmpeg -i {mp4_path} -c:v libx265 -preset medium -crf 28 -c:a aac -strict experimental -b:a 128k -movflags +faststart -y {mkv_path}')

    return jsonify({'The Video was downloaded in converted folder as': mkv_file})
@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['CONVERTED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

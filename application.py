from flask import Flask, request, render_template
app = Flask(__name__)

from inference import get_pokemon_name
import torchvision.transforms as transforms


@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html', value='hi')
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			print('file not uploaded')
			return
		file = request.files['file']
		image = file.read()
		pokemon_name = get_pokemon_name(image_bytes=image)
		return render_template('result.html', pokemon=pokemon_name)

if __name__ == '__main__':
	app.run(debug=True)

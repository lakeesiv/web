var notable_python_skills = "&ensp;&ensp;\"notable_python_skills\": [\"Tensorflow/Keras\", \"plotly\", \"SciPy\",\n\
		<span style=\"display:inline-block; width: 185pt;\"></span>\"Flask\", \"Dash\"],\n"

var stats = ["`{\n\
		&ensp;&ensp;\"name\": \"Lakeeshan (Lakee) Sivaraya\",\n\
		&ensp;&ensp;\"occupation\": \"1st Year Student\",\n\
		&ensp;&ensp;\"university\": \"University of Cambridge\",\n\
		&ensp;&ensp;\"subject\": \"Engineering\",\n\
		&ensp;&ensp;\"skills\": [\"Python\", \"Data Science\", \"Machine Learning\",\n \
		<span style=\"display:inline-block; width: 85pt;\"></span>\"LaTeX\", \"git\", \"HTML/CSS\", \"Javascript\"],\n\
		&ensp;&ensp;\"hobbies\": [\"Cooking\", \"Hydroponics\"]\n\
}`"]
var text = [
	"`~\\Desktop\\stats>`^1000 ls^1000\n `lakee.py`\n`~\\Desktop\\stats>`^1000 \
	python ^1000 \n `Python 3.8.3`\n `>>>`\
	^1000 <span style='color:#FF1493'>import</span> lakee ^1000 \n `>>>` ^1000 \
	<span style='color:#0080FF'>print(</span>\lakee\<span style='color:#0080FF'>.get_stats()</span>\<span style='color:#0080FF'>)</span>\
	^1000\n".concat(`${stats}`),
];

var typed6 = new Typed(".console", {
	strings: text,
	typeSpeed: 40,
	backSpeed: 0,
	loop: false,
	cursorChar: "_",
});

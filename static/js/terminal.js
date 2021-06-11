let data = {
  name: "Lakeeshan (Lakee) Sivaraya",
  occupation: "1st Year Student",
  university: "University of Cambridge",
  subject: "Engineering",
  skills: [
    "Python",
    "Data Science",
    "Machine Learning",
    "LaTeX",
    "git",
    "HTML/CSS",
    "Javascript",
  ],
  hobbies: ["Cooking", "Hydroponics"],
};

let stats = JSON.stringify(data, null, 4);
stats = "`" + stats + "`";
console.log(stats);
var text = [
  "`~\\Desktop\\stats>`^1000 ls^1000\n `lakee.py`\n`~\\Desktop\\stats>`^1000 python ^1000 \n `Python 3.8.3`\n `>>>`^1000 <span style='color:#FF1493'>import</span> lakee ^1000 \n `>>>` ^1000 <span style='color:#0080FF'>print(</span>lakee<span style='color:#0080FF'>.get_stats()</span><span style='color:#0080FF'>)</span>^1000\n".concat(
    `${stats}`
  ),
];

var typed6 = new Typed(".console", {
  strings: text,
  typeSpeed: 40,
  backSpeed: 0,
  loop: false,
  cursorChar: "_",
});

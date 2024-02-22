
//Js
document.querySelector(".mobile-btn").addEventListener("click", function () {
  document.querySelector(".menu").classList.toggle("active");
});




const modeToggle = document.getElementById('mode-toggle');
const l=document.getElementById('logo');
const lo=document.getElementById('l');

let isNightMode = true; // Set initial state to night mode

modeToggle.addEventListener('click', () => {
  // Toggle between day and night mode
  isNightMode = !isNightMode;

  // Change the image source based on the mode
  if (!isNightMode) {
    modeToggle.src = "/static/assets/img/day.png";
    l.src="/static/assets/img/logoblack.png"
    lo.src="/static/assets/img/logoblack.png"
    
    // Add styles for day mode
    document.body.classList.remove('night-mode');
    document.body.classList.add('day-mode');
  } else {
    modeToggle.src = "/static/assets/img/night.png";
    l.src="/static/assets/img/a.png";
    lo.src="/static/assets/img/a.png";
    // Add styles for night mode
    document.body.classList.remove('day-mode');
    document.body.classList.add('night-mode');
  }
});

// Initially set the image source and body class accordingly
if (isNightMode) {
  modeToggle.src = "/static/assets/img/night.png";
  l.src="/static/assets/img/a.png";
  lo.src="/static/assets/img/a.png";
  document.body.classList.add('night-mode');
} else {
  modeToggle.src = "/static/assets/img/day.png";
  l.src="/static/assets/img/logoblack.png";
  lo.src="/static/assets/img/logoblack.png";
  document.body.classList.add('day-mode');
}

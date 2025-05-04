// Rotating Post of the Day
const prompts = [
    "What's something kind a stranger has done for you?",
    "If your group had a theme song, what would it be?",
    "What does a good meetup look like to you?",
    "Describe a meaningful conversation you’ve had recently.",
    "What would you do if you had a free afternoon with friends?"
  ];
  
  const postElement = document.getElementById("post");
  if (postElement) {
    const random = Math.floor(Math.random() * prompts.length);
    postElement.textContent = prompts[random];
  }
  
  // RSVP Toggle Button
  function toggleRSVP(button) {
    if (button.textContent === "RSVP") {
      button.textContent = "✓ Going";
      button.style.backgroundColor = "green";
    } else {
      button.textContent = "RSVP";
      button.style.backgroundColor = "#4e8cff";
    }
  }
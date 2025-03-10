const express = require('express');
const path = require('path');
const app = express();
app.set('view engine', 'ejs');

// Serve static files (CSS, images, etc.) from the 'public' folder
app.use(express.static(path.join(__dirname, 'public')));

// Sample professor data
const professors = [
    {
        name: "Dr. Smith",
        department: "Computer Science",
        school: "North Carolina Agricultural and Technical State University",
        rating: 4.5
    },
    {
        name: "Dr. Johnson",
        department: "Computer Science",
        school: "North Carolina Agricultural and Technical State University",
        rating: 4.7
    },
    {
        name: "Dr. Lee",
        department: "Computer Science",
        school: "North Carolina Agricultural and Technical State University",
        rating: 4.3
    }
];

// Route for the student profile page
app.get('/student-profile', (req, res) => {
  const student = {
    name: "Niya Henderson",
    email: "nrhenderson@aggies.ncat.edu",
    major: "Computer Science",
    university: "North Carolina Agricultural and Technical State University",
    bio: "An aspiring software engineer with a passion for full-stack development and leadership.",
    profilePicture: "/images/niya-profile.jpg"  // Optional, use your image if desired
  };

  res.render('student-profile', { student });
});



// Route for homepage (index.html)
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// Route for the professors page
app.get('/professors', (req, res) => {
    res.render('professors', { professors: professors });
});

// Set up the view engine (we'll use EJS for rendering dynamic content)
app.set('view engine', 'ejs');

// Start the server
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});

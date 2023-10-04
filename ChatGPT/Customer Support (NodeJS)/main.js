const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000

// Set the view engine to EJS
app.set('view engine', 'ejs');
app.use(express.json());
app.use(express.static(__dirname + '/public'))

app.get('/', (req, res) => {
    res.render('index'); 
})

app.post('/ask', async (req, res) => {
    const question = req.body.question;
    try {
        const response = await axios.post('http://127.0.0.1:5000/ask', { question});
        res.render('answer', {answer : response.data.answer })
        console.log('Response data:', response.data.answer);
    } catch (error) {
        console.error('Error fetching data - Status:', error.response.status, 'Message:', error.response.statusText);
        res.status(500).send('Error fetching data from the API. Please try again later.');
    }
})
app.listen(port,()=>{
    console.log('Running on port',port)
})

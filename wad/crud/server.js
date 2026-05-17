const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Middleware to parse incoming JSON payloads
app.use(cors());
app.use(express.json());

// 1. MongoDB Connection Setup
// Connects to your local MongoDB server and creates a database named 'assignmentDB'
mongoose.connect('mongodb://127.0.0.1:27017/assignmentDB')
    .then(() => console.log('Connected to MongoDB successfully.'))
    .catch(err => console.error('MongoDB connection error:', err));

// 2. Define the Database Schema & Model
const AssignmentSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: String,
    score: Number
});
const Assignment = mongoose.model('Assignment', AssignmentSchema);


// --- THE FOUR CRUD API ENDPOINTS ---

// [CREATE] - POST Request
app.post('/api/assignments', async (req, res) => {
    try {
        const newAssignment = new Assignment(req.body);
        const savedAssignment = await newAssignment.save();
        res.status(201).json(savedAssignment);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// [READ] - GET Request (Fetches all records)
app.get('/api/assignments', async (req, res) => {
    try {
        const assignments = await Assignment.find();
        res.status(200).json(assignments);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// [UPDATE] - PUT Request (Modifies a specific record via its unique ID)
app.put('/api/assignments/:id', async (req, res) => {
    try {
        const updatedAssignment = await Assignment.findByIdAndUpdate(
            req.params.id,
            req.body,
            { new: true, runValidators: true } // Returns the newly modified data
        );
        if (!updatedAssignment) return res.status(404).json({ error: 'Assignment not found' });
        res.status(200).json(updatedAssignment);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

// [DELETE] - DELETE Request (Removes a specific record via its unique ID)
app.delete('/api/assignments/:id', async (req, res) => {
    try {
        const deletedAssignment = await Assignment.findByIdAndDelete(req.params.id);
        if (!deletedAssignment) return res.status(404).json({ error: 'Assignment not found' });
        res.status(200).json({ message: 'Assignment successfully deleted' });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Start the Backend Server
app.listen(PORT, () => {
    console.log(`Backend CRUD server running at http://localhost:${PORT}`);
});
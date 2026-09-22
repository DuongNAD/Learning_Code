import { GoogleGenAI } from '@google/genai';
import dotenv from 'dotenv';

dotenv.config();

const apiKey = process.env.GEMINI_API_KEY;
console.log('API Key length:', apiKey ? apiKey.length : 0);
console.log('API Key starts with:', apiKey ? apiKey.substring(0, 5) : 'none');

const ai = new GoogleGenAI({ apiKey });

async function runTest() {
    try {
        const response = await ai.models.generateContent({
            model: 'models/gemini-2.5-flash',
            contents: [{ role: 'user', parts: [{ text: 'Say hi' }] }],
        });
        console.log('Success:', response.text);
    } catch (error: any) {
        console.error('Error testing API:', error.message);
    }
}

runTest();

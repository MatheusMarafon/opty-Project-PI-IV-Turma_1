/*
* This is the bridge of React application and Browser.
*/

/* --- IMPORTS --- */
import './index.css';
import App from './App.tsx';
import { createRoot } from 'react-dom/client';


/* --- CODE --- */
createRoot(document.getElementById('root')!).render(<App />);

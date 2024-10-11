import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Orders} from "./components/Orders";

function App() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<Orders/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;

import './App.css';
import Home from './Components/Home'; 
import Template from './Components/Template_Page';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<Home/>} /> {/* Home 作为默认聊天页面 */}
      <Route path="/template" element={<Template/>}></Route>
      </Routes>
    </Router>

  );
}

export default App;

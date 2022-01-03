import './App.css';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Register />
        <Login />
      </header>
    </div>
  );
}

export default App;

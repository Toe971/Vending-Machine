import logo from './logo.svg';
import './App.css';
import Logic from './Components/Logic';

/* 100 cents is 1 dollar coin */
const coins = ["10", "20", "50", "100"]
/*
below map returns object, implicit object return by wrapping {} within a ()
coins.map(coin => ({

})) 
totalCoins is a hardcoded object
*/
const totalCoins = coins.map(coin => ({
  
})) 

const checkCash = () => {
  
}

function App() {
  return (
    <div className="App">
      <h1>Vending Machine</h1>
    </div>
  );
}

export default App;

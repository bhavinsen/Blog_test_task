import './App.css';
import React, { useState } from "react";


function App() {
  

  // Set the initial count state to zero, 0
  const [count, setCount] = useState(0);

  // Create handleIncrement event handler
  const handleIncrement = () => {
    setCount(prevCount => prevCount + 1);
  };

  
  return (
    <div>
      <div className='center'>
        
        <button className='button' onClick={handleIncrement}>Click Count: {count}</button><br/><br/>
      <button onClick={() => setCount(0)}>Reset</button>

      </div>
    </div>
  );
}


export default App;

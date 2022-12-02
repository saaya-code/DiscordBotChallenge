import { useState, useEffect } from 'react'
//import styles from '../index'
import reactLogo from './assets/react.svg'
import './App.css'

function App() {
  //const [styles, setStyles] = useState({})
  useEffect(()=>{
    console.log('i fire once');
    fetch("http://localhost:3000",{
      method: "GET"
    }).then((response)=>{
      if(response.ok){
        return response.json()
      }
    }).then((data)=>{    
      if("background-color" in data){
        document.body.style.backgroundColor = data["background-color"]
    }
    if("addText" in data){
      const para = document.createElement("p")
      para.innerText = data["addText"];
      document.body.appendChild(para);
    }
    if("TextColor" in data){
      document.body.style.color = data["TextColor"]
    }
  })

  },[])

  return (
    <div className='main-content'>
      <h1>Welcome traveler!</h1>
      </div>
  )
}

export default App

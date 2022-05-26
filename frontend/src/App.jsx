import React, { useState, useEffect } from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';

export const App = () => {
  const [count, setCount] = useState(0)
  const [data, setData] = useState()

  useEffect(() => {
    axios.get('http://localhost:5000/user').then(
      res => {
        setData(res.data.user)
        console.log(res.data)
      }
    )
  }, [count])

  const onClickButton = () => {
    setCount(count + 1);
  };

  return (
    <div className="card">
      <div className="card-body">
        <h2>こんにちは、{ data }さん</h2>
        <Button onClick={onClickButton} variant="outline-primary">+{ count }</Button>
      </div>
    </div>
  )
};


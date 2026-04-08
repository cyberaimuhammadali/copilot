import React, {useEffect, useState} from "react";
import axios from "axios";

export default function Menu(){
  const [items, setItems] = useState([]);
  useEffect(()=> {
    axios.get(`${import.meta.env.VITE_API_URL}/menu`).then(r=>setItems(r.data));
  },[]);
  const addToCart = (item) => {
    const cart = JSON.parse(localStorage.getItem("cart")||"[]");
    cart.push({...item, qty:1});
    localStorage.setItem("cart", JSON.stringify(cart));
    alert("Savatga qo‘shildi");
  };
  return (
    <div className="menu">
      {items.map(it=>(
        <div key={it.id} className="card">
          <img src={it.photo||"/placeholder.png"} alt={it.name}/>
          <h3>{it.name}</h3>
          <p>{it.price} UZS</p>
          <button onClick={()=>addToCart(it)}>Savatga qo‘shish</button>
        </div>
      ))}
      <a className="checkout" href="#" onClick={()=>{
        const cart = localStorage.getItem("cart");
        // send to bot via Telegram WebApp if available
        if(window.Telegram && window.Telegram.WebApp){
          window.Telegram.WebApp.sendData(cart);
        } else {
          alert("Iltimos, Telegram ichida oching.");
        }
      }}>Checkout</a>
    </div>
  );
}

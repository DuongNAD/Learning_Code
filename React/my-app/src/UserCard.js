import React from 'react';

function UserCard(props) {

  const handleClick = () =>{
    alert(`Xin chao, so thich cua toi la ${props.text}`);
  };
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px' }}>
      <h3>Text: {props.text}</h3>
      <button onClick={handleClick}>Gui loi chao</button>
    </div>
  );
}

export default UserCard;

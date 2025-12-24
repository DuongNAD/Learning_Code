import React from 'react';

// Component này nhận props từ App.js để hiển thị nội dung công việc
function TodoItem(props) {
  return (
    <div style={{ 
      border: '1px solid #ddd', 
      padding: '10px', 
      marginTop: '10px', 
      borderRadius: '5px' 
    }}>
      <p>{props.text}</p>
    </div>
  );
}

export default TodoItem;
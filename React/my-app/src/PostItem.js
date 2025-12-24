
import React from 'react';

function PostItem({ title, content }) {
  return (
    <div style={{ border: '1px solid #ddd', padding: '10px', marginBottom: '5px', borderRadius: '4px' }}>
      <h4>{title}</h4>
      <p>{content}</p>
    </div>
  );
}

export default PostItem;